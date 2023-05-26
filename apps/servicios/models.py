from tabnanny import verbose
from django.db import models


class DatosServicios(models.Model):    
    direccion = models.CharField(max_length=50, null=True, blank=True)
    URL_ubicacion = models.URLField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    URL_instagram = models.URLField(max_length=200, null=True, blank=True)
    mail = models.EmailField(max_length=50, null=True, blank=True)



# Create your models here.
class ServiciosCategorias(models.Model):
    rubro = models.CharField(max_length=50)
    servicio = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    id_datos = models.ForeignKey(DatosServicios, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name = 'Categoría de servicios'
        verbose_name_plural = 'Categorías de servicios'

    def __str__(self):
        return f"{self.rubro} - {self.servicio}"        

    

