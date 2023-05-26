from django import forms

from . import models


class ServiciosCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.ServiciosCategorias
        fields = "__all__"
        