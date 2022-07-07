from datetime import datetime, timedelta
from django.conf import settings
from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .forms import EndpointForm
from django.contrib import messages
import uuid
from django.http import HttpResponseNotFound, HttpResponse
import pdb
import json

# Create your views here.
def home(request):
	remover_endpoints_antigos()

	data = {}
	data['base_route'] = genarate_base_route(request)
	data['site_url'] = settings.SITE_URL

	endpoints = Endpoint.objects.filter(base_route=data['base_route'])
	data['endpoints'] = endpoints

	return render(request, 'endpoint_manager/home.html', data)

def remover_endpoints_antigos():
	hoje = datetime.now().date()
	dataAntiga = hoje - timedelta(7)
	objects = Endpoint.objects.filter(Q(created_at__lt=dataAntiga) | Q(created_at__isnull=True))
	objects.delete()


def endpoint_retorno(request):
	paths = request.get_full_path().split('/')
	del paths[0]
	del paths[0]

	base_url_request = paths[0]
	del paths[0]

	endpoint_request = '/'.join(paths)

	endpoint = Endpoint.objects.filter(endpoint=endpoint_request, base_route=base_url_request).first()

	if not endpoint:
		return HttpResponseNotFound()

	content_type_result = 'application/json'
	if endpoint.tipo_retorno == RetornosRequisicao.XML.value:
		content_type_result = 'application/xml'

	return HttpResponse(endpoint.retorno, content_type=content_type_result, status=endpoint.status_code)

	# return redirect('/')

def remover_endpoints(request):
	if 'base_route' not in request.session:
		messages.error(request, 'Erro na busca de endpoints', extra_tags='danger')
		return redirect('/')

	if request.GET.get('id'):
		objects = Endpoint.objects.filter(base_route=request.session['base_route'], id=request.GET.get('id'))
	else:
		objects = Endpoint.objects.filter(base_route=request.session['base_route'])

	objects_number = objects.count()

	if objects_number <= 0:
		messages.error(request, 'Não há endpoints para excluir', extra_tags='danger')
		return redirect('/')

	objects.delete()
	messages.success(request, 'Endpoint(s) excluído(s) com sucesso')
	return redirect('/')

def novo_endpoint(request):
	data = {}

	form = EndpointForm(request.POST or None)
	if form.is_valid():
		form.instance.base_route = genarate_base_route(request)
		form.save()
		messages.success(request, 'Endpoint cadastrado com sucesso')
		return redirect('/')

	data['form'] = form

	return render(request, 'endpoint_manager/novoendpoint_pagina.html', data)

def genarate_base_route(request):
	if 'base_route' not in request.session:
		request.session['base_route'] = uuid_generator()

	# Pega o valor da sessão, seta o valor da chave como padrão se  não estiver presente.
	return request.session['base_route']

def uuid_generator(string_length=10):
	"""Returns a random string of length string_length."""
	random = str(uuid.uuid4()) # Convert UUID format to a Python string.
	random = random.upper() # Make all characters uppercase.
	random = random.replace("-","") # Remove the UUID '-'.
	return random[0:string_length] # Return the random string.