from django.db import models

class Artist(models.Model):
	name = models.CharField(max_length=100)
	birthday = models.DateField()

class Film(models.Model):
	name = models.CharField(max_length=100)
	director_name = models.CharField(max_length=100)
	year = models.IntegerField()
	productor_name = models.CharField(max_length=100)
	artists = models.ManyToManyField(Artist)
	grade = models.FloatField()