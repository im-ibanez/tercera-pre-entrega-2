from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "servicios/index.html")

# Create your views here.
# def servicios_categoria_list(request):
#     categorias = models.ServiciosCategorias.objects.all()
#     context = {"categorias": categorias}
#     return render(request, "servicios/servicios_categoria_list.html", context)


class ServiciosCategoriasList(ListView):
    model = models.ServiciosCategorias


# def servicios_categoria_create(request):
#     if request.method == "POST":
#         form = forms.ServiciosCategoriasForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("servicios:index")
#     else:
#         form = forms.ServiciosCategoriasForm()
#     return render(request, "servicios/servicios_categoria_create.html", {"form": form})


class ServiciosCategoriasCreate(CreateView):
    model = models.ServiciosCategorias
    form_class = forms.ServiciosCategoriasForm
    success_url = reverse_lazy("servicios:index")


# def servicios_categoria_delete(request, id):
#     categoria = models.ServiciosCategorias.objects.get(id=id)
#     if request.method == "POST":
#         categoria.delete()
#         return redirect("servicios:servicios_categoria_list")
#     return render(request, "servicios/servicios_categoria_delete.html", {"categoria": categoria})


class ServiciosCategoriasDelete(DeleteView):
    model = models.ServiciosCategorias
    success_url = reverse_lazy("servicios:servicioscategoria_list")


# def servicios_categoria_update(request, id):
#     categoria = models.ServiciosCategorias.objects.get(id=id)
#     if request.method == "POST":
#         form = forms.ServiciosCategoriasForm(request.POST, instance=categoria)
#         if form.is_valid():
#             form.save()
#             return redirect("servicios:servicios_categoria_list")
#     else:
#         form = forms.ServiciosCategoriasForm(instance=categoria)
#     return render(request, "servicios/servicios_categoria_update.html", {"form": form})


class ServiciosCategoriasUpdate(UpdateView):
    model = models.ServiciosCategorias
    success_url = reverse_lazy("servicios:servicioscategoria_list")
    form_class = forms.ServiciosCategoriasForm


class ServiciosCategoriasDetail(DetailView):
    model = models.ServiciosCategorias