from pyexpat import model
from django.db import models
from enum import Enum

# Create your models here.

class MetodosRequisicao(Enum):
	GET = 'GET'
	POST = 'POST'
	PUT = 'PUT'
	DELETE = 'DELETE'
	PATCH = 'PATCH'

class RetornosRequisicao(Enum):
	JSON = 'JSON'
	XML = 'XML'

class Api(models.Model):
    base_route = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Endpoint(models.Model):
	METODOS_REQUISICAO = (
        ('GET', MetodosRequisicao.GET.value),
        ('POST', MetodosRequisicao.POST.value),
        ('PUT', MetodosRequisicao.PUT.value),
        ('DELETE', MetodosRequisicao.DELETE.value),
        ('PATCH', MetodosRequisicao.PATCH.value)
    )

	TIPO_RETORNO = (
		('JSON', RetornosRequisicao.JSON.value),
		('XML', RetornosRequisicao.XML.value)
	)

	endpoint = models.CharField(max_length=90, default='', unique=True)
	status_code = models.IntegerField(default=200)
	metodo_http = models.CharField(max_length=10, choices=METODOS_REQUISICAO, default=MetodosRequisicao.GET.value)
	tipo_retorno = models.CharField(max_length=10, choices=TIPO_RETORNO, default=RetornosRequisicao.JSON.value)
	retorno = models.TextField()