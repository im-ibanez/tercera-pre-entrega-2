from django.urls import path

from . import views

# *********** URLS basadas en funciones
# urlpatterns = [
#     path("", views.index, name="index"),
#     path("servicios_categorias_listado/", views.servicios_categorias_list, name="servicios_categorias_list"),
#     path("servicios_categorias_create/", views.servicios_categorias_create, name="servicios_categorias_create"),
#     path("servicios_categorias_delete/<int:id>", views.servicios_categorias_delete, name="servicios_categorias_delete"),
#     path("servicios_categorias_update/<int:id>", views.servicios_categorias_delete, name="servicios_categorias_delete"),
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
