from django.shortcuts import render

from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from reviewsESentimentos import settings
from .models import Reviews
from requests import serializer
# Create your views here.
def request_reviews(request):
		#o link pra o outro tá no html
		return render(request,'home.html', {})

def show_reviews(request):
	if request.method == 'POST':
		parametrobusca = request.POST['palavra_chave']
		api_key = '8eb260cbb899f0bfdef87b8aca2446cb:1:73436343'
		r = request.get('http://api.nytimes.com/svc/movies/v2/reviews/search.json?query='+str(parametrobusca)+'api-key='+api_key)
		serializer = EmbedSerializer(data=r.DATA)
		content = JSONRenderer().render(serializer.data)
	#essas linhas devem ser descomentadas quando blog for implementado e as categorias puxadas dele
	#test = Test.objects.get(id=test_id)
 		
		return render(request, 'respostas.html',content)
	elif request.method == 'GET':
		return render(request,'home.html',{})