from datetime import datetime
from django.shortcuts import render

# Create your views here.
def home(request):
	data = {}

	data['now'] = datetime.now()

	# return HttpResponse(html)
	return render(request, 'endpoint_manager/home.html', data)