from django.contrib import admin

from . import models

# admin.site.register(models.ProductoCategoria)


@admin.register(models.ServiciosCategorias)
class ServiciosCategoriaAdmin(admin.ModelAdmin):
    list_display = ("rubro", "servicio", "nombre")
    search_fields = ("servicio",)
    list_filter = ("servicio",)
    ordering = ("servicio",)
