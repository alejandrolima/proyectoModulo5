"""proyectoa_agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from  app_contactos.serialisables import CategoriasViewSet
from rest_framework import response,request
from app_contactos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
 
    #Mostrar todos los registros en una tabla
    path('app_contactos/', ContactoListar.as_view(template_name = "app_contactos/index.html"), name='listar'),
 
    #Mostrar una página con el detalle del registro
    path('app_contactos/detalle/<int:pk>', ContactoDetalle.as_view(template_name = "app_contactos/detalles.html"), name='detalles'),
 
    #Mostrar formulario de alta de nuevo registro
    path('app_contactos/nuevo', ContactoNuevo.as_view(template_name = "app_contactos/crear.html"), name='nuevo'),
 
    #Mostrar formulario de modificación de registro
    path('app_contactos/editar/<int:pk>', ContactoActualizar.as_view(template_name = "app_contactos/actualizar.html"), name='actualizar'), 
 
    #Eliminar un registro
    path('app_contactos/eliminar/<int:pk>', ContactoEliminar.as_view(), name='eliminar'),    

    #Redirección a html Cerrar Sesión (logout.html)
    #Sólo ejemplo para mostrar una página HTML estática
    path('app_contactos/cerrarsesion', CerrarSesion, name='cerrarsesion'),	

    path(
        'categoria/',
        CategoriasViewSet.as_view({'get': 'retrieve'}),
        name='categorias'
    ),

    path('api/categorias', getCategorias),
    path('api/contactos', getContactos),
    path('api/productos', getProductos),
    path('api/ventas', getVentas),

]
