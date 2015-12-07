from django.shortcuts import render

from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from reviewsESentimentos import settings
import os

# Create your views here.
def home(request):
	#essas linhas devem ser descomentadas quando blog for implementado e as categorias puxadas dele
	#test = Test.objects.get(id=test_id)
	#context = {}
	return render(request,'home.html',{})
	#return HttpResponse(maybe)