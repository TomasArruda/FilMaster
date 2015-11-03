from django.shortcuts import render
from infila.models import Film, Artist
from infila.serializers import FilmSerializer, ArtitstSerializer

class FilmViewSet(viewsets.ModelViewSet):
	queryset = Film.objects.all()
	serializer_class = FilmSerializer

class ArtistViewSet(viewsets.ModelViewSet):
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer