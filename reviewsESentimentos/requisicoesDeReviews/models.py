from django.db import models

# Create your models here.

class Reviews (models.Model):
	text = models.TextField()