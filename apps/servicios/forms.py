from django import forms

from . import models


class ServiciosCategoriasForm(forms.ModelForm):
    class Meta:
        model = models.ServiciosCategorias
        fields = "__all__"
