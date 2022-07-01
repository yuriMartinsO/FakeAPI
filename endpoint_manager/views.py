from datetime import datetime
from django.shortcuts import render, redirect
from .forms import EndpointForm
from django.contrib import messages
import uuid

# Create your views here.
def home(request):
	data = {}
	data['api_url'] = generate_api_url(request)

	return render(request, 'endpoint_manager/home.html', data)

def novo_endpoint(request):
	data = {}

	form = EndpointForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Endpoint cadastrado com sucesso')
		return redirect('/')

	data['form'] = form

	return render(request, 'endpoint_manager/novoendpoint_pagina.html', data)

def generate_api_url(request):
	if 'api_url' not in request.session:
		request.session['api_url'] = id_generator()

	# Pega o valor da sessão, seta o valor da chave como padrão se  não estiver presente.
	return request.session['api_url']

def id_generator(string_length=10):
	"""Returns a random string of length string_length."""
	random = str(uuid.uuid4()) # Convert UUID format to a Python string.
	random = random.upper() # Make all characters uppercase.
	random = random.replace("-","") # Remove the UUID '-'.
	return random[0:string_length] # Return the random string.