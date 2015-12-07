from rest_framework import serializers
from .models import Reviews

class EmbedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews