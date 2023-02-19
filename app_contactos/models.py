from django.db import models
from django.utils import timezone

class Contactos(models.Model):
	nombre = models.CharField(max_length=150, null=False, verbose_name="Nombre", default="")
	telefono_movil = models.CharField(max_length=9, null=True, blank=True, verbose_name="Tlfno. móvil", default="")
	telefono_fijo = models.CharField(max_length=9, null=True, blank=True, verbose_name="Tlfno. fijo", default="+34")
	mail = models.EmailField(max_length=150, null=True, blank=True, verbose_name="EMail", default="")
	direccion = models.CharField(max_length=200, null=True, blank=True, verbose_name="Dirección postal", default="")	
	foto = models.FileField(max_length=254, null=True, blank=True, verbose_name="Foto")
	empresa = models.CharField(max_length=150, default='Proyecto A')
	fecha_alta = models.DateTimeField(auto_now_add=True)
	fecha_actualizacion = models.DateTimeField(auto_now=True)
 
class Meta:	 db_table = 'contactos' 

class Categorias(models.Model):
	nombre = models.CharField(max_length=150, null=False, verbose_name="Nombre", default="")
	descripcion = models.CharField(max_length=200, null=True, blank=True, verbose_name="Descripcion", default="")
	fecha_alta = models.DateTimeField(auto_now_add=True)
	fecha_actualizacion = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.nombre

class Meta:	 db_table = 'categorias' 

class Productos(models.Model):
	nombre = models.CharField(max_length=150, null=False, verbose_name="Nombre", default="")
	descripcion = models.CharField(max_length=9, null=True, blank=True, verbose_name="Descripcion", default="")
	categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
	precio = models.DecimalField(decimal_places=2,null=False, verbose_name="Precio", max_digits=10)
	unidades = models.CharField(max_length = 3,null=False, verbose_name="Unidades", default = "")
	fecha_alta = models.DateTimeField(auto_now_add=True)
	fecha_actualizacion = models.DateTimeField(auto_now=True)
 
class Meta:	 db_table = 'productos' 

class Ventas(models.Model):
	producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
	contacto = models.ForeignKey(Contactos, on_delete=models.CASCADE)
	total = models.DecimalField(decimal_places=2,null=False, verbose_name="total", max_digits=100)
	descuento = models.DecimalField(decimal_places=2,null=False, verbose_name="descuento", max_digits=100)
	totalventa = models.DecimalField(decimal_places=2,null=False, verbose_name="totalventa", max_digits=100)
	fecha_alta = models.DateTimeField(auto_now_add=True)
	fecha_actualizacion = models.DateTimeField(auto_now=True)
 
class Meta:	 db_table = 'ventas' 