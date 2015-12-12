# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from reviewsESentimentos import settings
from .models import Reviews
import requests
from .serializer import EmbedSerializer
from django.core import serializers
from HTMLParser import HTMLParser
from analyser import Analyser

# Create your views here.
@csrf_exempt
def request_reviews(request):
		#o link pra o outro tá no html
		return render(request,'home.html', {})

@csrf_exempt
def analise(request):
	if request.method == 'POST':
		a = Analyser(1,2)
		content = show_reviews(request)

		a.analyse(content['reviews'])
		
		return render(request, 'respostas.html',content)
	elif request.method == 'GET':
		return render(request,'home.html',{})

@csrf_exempt
def show_reviews(request):
	jogo = request.POST['jogo']
	limite = request.POST['limite']
	api_key = 'a08006130f125bc5ade2af9f53ccdb10a5581460'
	limit = "&limit="+(limite)
	#1o pegar os releases do jogo

	urlreleases = "http://www.giantbomb.com/api/game/"+str(jogo)+"/?api_key="+(api_key)+"&format=json&field_list=releases"
	r = requests.get(urlreleases)
	soResultados = r.json().get('results')
	soReleases = soResultados.get('releases') #aqui cheguei na lista de dicionarios
	listaCodigosReleases = []
	for elem in soReleases:
		listaCodigosReleases.append(elem.get('id'))
	#fim de pegar o codigo das releases
	print(listaCodigosReleases)
	#2o pegar reviews de cada release
	urlreviews = "http://www.giantbomb.com/api/user_reviews/?api_key="+(api_key)+"&format=json&filter=object:3050-"#falta por o resto do id
	listaReviews = []
	for elem in listaCodigosReleases:
		urltemp = urlreviews+str(elem)
		s = requests.get(urltemp)
		revs = s.json().get('results')
		for elem2 in revs:
			listaReviews.append(strip_tags(elem2.get('description')))
	#Nessa altura do campeonato temos uma lista com tds os reviews em forma de string
	#chamada listaReviews, faça com ela o que quiser, tomás
	content = {'reviews':listaReviews[:int(limite)]}
	return content

class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.strict = False
		self.convert_charrefs= True
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)

def strip_tags(html):
	s = MLStripper()
	if html != None:
		s.feed(html)
	return s.get_data()