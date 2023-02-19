from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import serializers

from app_contactos.models import Categorias

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categorias
        fields = ['nombre', 'descripcion', 'fecha_alta', 'fecha_actualizacion']

class CategoriasViewSet(viewsets.ModelViewSet):

  queryset = Categorias.objects.all()
  serializer_class = CategoriaSerializer
