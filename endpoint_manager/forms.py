from django.forms import ModelForm
from .models import Endpoint

class EndpointForm(ModelForm):
	class Meta:
		model = Endpoint
		fields = ['endpoint', 'status_code', 'metodo_http', 'tipo_retorno', 'retorno']