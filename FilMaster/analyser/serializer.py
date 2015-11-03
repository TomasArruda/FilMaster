from django.contrib.auth.models import Film, Artist
from rest_framework import serializers
from models import Film, Artist

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'name', 'director_name', 'year', 'produtor_name', 'artists', 'grade')

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'birthday')