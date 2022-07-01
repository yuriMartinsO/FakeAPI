from datetime import datetime
from django.shortcuts import render, redirect
from .forms import EndpointForm
from django.contrib import messages

# Create your views here.
def home(request):
	data = {}

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