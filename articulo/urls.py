from django.urls import path
from . import views

urlpatterns = [
    path("agregar/",views.articulo_agregar,name='articulo_agregar'),
    path("delete/",views.delete_articulo,name='articulo_delete'),

    path("listar/",views.listar_articulo,name='articulo_listar'),
    path("movimiento/",views.articulo_mover,name='articulo_movimiento'),
    path("listar/",views.listar_movimiento,name='movimiento_listar'),



]
