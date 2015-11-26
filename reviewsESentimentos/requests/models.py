from django.db import models

# Create your models here.

class Reviews (models.Model):
	text = models.TextField()
	author = models.CharField(max_length=50)
	gender = models.CharField(max_length=50)