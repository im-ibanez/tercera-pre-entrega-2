from django.urls import path

from . import views

# *********** URLS basadas en funciones
# urlpatterns = [
#     path("", views.index, name="index"),
#     path("producto_categoria_listado/", views.producto_categoria_list, name="producto_categoria_list"),
#     path("producto_categoria_create/", views.producto_categoria_create, name="producto_categoria_create"),
#     path("producto_categoria_delete/<int:id>", views.producto_categoria_delete, name="producto_categoria_delete"),
#     path("producto_categoria_update/<int:id>", views.producto_categoria_delete, name="producto_categoria_delete"),
# ]

# *********** URLS basadas en clases
urlpatterns = [
    path("", views.index, name="index"),
    path("servicioscategorias/list/", views.ServiciosCategoriasList.as_view(), name="servicioscategorias_list"),
    path("servicioscategorias/create/", views.ServiciosCategoriasCreate.as_view(), name="servicioscategorias_create"),
    # ! De forma predeterminada, las URLs basadas en clases reciben pk, no id.
    path(
        "servicioscategorias/delete/<int:pk>", views.ServiciosCategoriasDelete.as_view(), name="servicioscategorias_delete"
    ),
    # ! De forma predeterminada, las URLs basadas en clases reciben pk, no id.
    path(
        "servicioscategorias/update/<int:pk>", views.ServiciosCategoriasUpdate.as_view(), name="servicioscategorias_update"
    ),
    path(
        "servicioscategorias/detail/<int:pk>", views.ServiciosCategoriasDetail.as_view(), name="servicioscategorias_detail"
    ),
]
