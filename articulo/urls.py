from django.urls import path
from . import views

urlpatterns = [
    path("agregar/",views.articulo_agregar,name='articulo_agregar'),
    path ('delete/<int:id_articulo>/',views.delete_articulo,name='articulo_delete'),

    path("listar_articulo/",views.listar_articulo,name='articulo_listar'),
    path('<int:id_articulo>/', views.articulo_agregar,name='articulo_update'), # get and post req. for update operation

    # path("movimiento/",views.articulo_mover,name='articulo_movimiento'),
    # path("listar/",views.listar_movimiento,name='movimiento_listar'),



]
