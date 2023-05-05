from rest_framework import viewsets
from app.api import serializers
from app import models

class AcoesViewset(viewsets.ModelViewSet):
    serializer_class = serializers.AcoesSerializer
    queryset = models.Acoes.objects.all()