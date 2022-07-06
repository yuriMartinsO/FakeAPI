from datetime import datetime
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Endpoint
from .forms import EndpointForm
from django.contrib import messages
import uuid
import pdb

# Create your views here.
def home(request):
	data = {}
	data['base_route'] = genarate_base_route(request)
	data['site_url'] = settings.SITE_URL

	return render(request, 'endpoint_manager/home.html', data)

def remover_endpoints(request):
	if 'base_route' not in request.session:
		messages.error(request, 'Erro na busca de endpoints', extra_tags='danger')
		return redirect('/')

	# request.session['base_route']
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