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

# Create your views here.
@csrf_exempt
def request_reviews(request):
		#o link pra o outro tá no html
		return render(request,'home.html', {})

@csrf_exempt
def show_reviews(request):
	if request.method == 'POST':
		jogo = request.POST['jogo']
		limite = request.POST['limite']
		api_key = 'a08006130f125bc5ade2af9f53ccdb10a5581460'
		urljson = "http://www.giantbomb.com/api/user_reviews/"+str(jogo)+"/?api_key="+(api_key)+"&format=json&limit="+(limite)+"&field_list=description"
		r = requests.get(urljson)
		listaDicts = r.json().get('results')
		novalista = []
		for elem in listaDicts:
			novalista.append(strip_tags(elem.get('description')))
		#Nessa altura do campeonato temos uma lista com tds os reviews em forma de string
		#chamada novalista, faça com ela o que quiser, tomás
		content = {'reviews':novalista}
		#/\esse é o dicionário q tem q ser passado pra pag html, favor trabalhar com a lista acima e n com ele :P
		#só queria bulir nele qnd os meninos entregassem a tela pronta
		return render(request, 'respostas.html',content)
	elif request.method == 'GET':
		return render(request,'home.html',{})

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
	s.feed(html)
	return s.get_data()