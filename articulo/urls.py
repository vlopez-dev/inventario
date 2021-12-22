from django.urls import path
from . import views

urlpatterns = [
    path("agregar/",views.articulo_agregar,name='articulo_agregar'),
    path ('delete/<int:id_articulo>/',views.delete_articulo,name='articulo_delete'),

    path("movimiento/",views.movimiento,name='movimiento'),
    path("listar_movimientos/",views.listar_movimientos,name='movimientos_listar'),
    path ('delete_mov/<int:id_movimiento>/',views.delete_movimientos,name='movimiento_delete'),
    path('<int:id_movimiento>/', views.movimiento,name='movimiento_update'),


    path("listar_articulo/",views.listar_articulo,name='articulo_listar'),
    path('<int:id_articulo>/', views.articulo_agregar,name='articulo_update'), # get and post req. for update operation

    # path("movimiento/",views.articulo_mover,name='articulo_movimiento'),
    # path("listar/",views.listar_movimiento,name='movimiento_listar'),

    path("stock/",views.filtro_stock,name='stock'),
    # path("stock_area/",views.filtro_stock_area,name='stock_area'),



]
