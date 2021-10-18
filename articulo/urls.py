from django.urls import path
from . import views

urlpatterns = [
    path("agregar/",views.articulo_agregar,name='agregar'),
    path("delete/",views.delete_articulo,name='delete'),

    path("listar/",views.listar_articulo,name='listar'),
    path("movimiento/",views.articulo_mover,name='movimiento'),
    path("listar/",views.listar_movimiento,name='movimiento'),



]
