from django import forms
from .models import Endpoint

class EndpointForm(forms.ModelForm):
	class Meta:
		model = Endpoint
		fields = ['endpoint', 'status_code', 'metodo_http', 'tipo_retorno', 'retorno']