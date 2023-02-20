from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import serializers

from app_contactos.models import *

#categorias
class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categorias
        fields = ['nombre', 'descripcion', 'fecha_alta', 'fecha_actualizacion']

class CategoriasViewSet(viewsets.ModelViewSet):

  queryset = Categorias.objects.all()
  serializer_class = CategoriaSerializer
  
  #contactos
class ContactoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contactos
        fields = ['nombre', 'telefono_movil', 'telefono_fijo', 'mail','foto', 'empresa', 'fecha_alta', 'fecha_actualizacion']

class ContactosViewSet(viewsets.ModelViewSet):

  queryset = Contactos.objects.all()
  serializer_class = ContactoSerializer
  
#productos
class ProductosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion', 'categoria', 'precio','unidades', 'fecha_alta', 'fecha_actualizacion']

class ProductosViewSet(viewsets.ModelViewSet):

  queryset = Productos.objects.all()
  serializer_class = ProductosSerializer
  
#ventas
class VentasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ventas
        fields = ['producto', 'contacto', 'total', 'descuento','totalventa', 'fecha_alta', 'fecha_actualizacion']

class VentasViewSet(viewsets.ModelViewSet):

  queryset = Ventas.objects.all()
  serializer_class = VentasSerializer
