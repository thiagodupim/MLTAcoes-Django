from rest_framework import serializers
from app import models

class AcoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Acoes
        fields = '__all__'