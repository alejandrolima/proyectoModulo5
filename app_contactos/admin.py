from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categorias, Productos


@admin.register(Categorias)
class CategoriaAdmin(admin.ModelAdmin):
    #exclude = ["usuario_actualizacion", "transaccion"]
    list_display = ['nombre', 'descripcion', 'fecha_alta', 'fecha_actualizacion']
    search_fields = ['nombre', 'descripcion']
@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    #exclude = ["usuario_actualizacion", "transaccion"]

    list_display = ['nombre', 'descripcion','categoria', 'precio','unidades','fecha_alta', 'fecha_actualizacion']
    search_fields = ['nombre', 'descripcion']
    #filter_horizontal = ['nombre', 'descripcion']