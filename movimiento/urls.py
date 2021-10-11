from django.urls import path
from . import views

urlpatterns = [
    path("agregar/",views.movimiento_agregar,name='agregar'),
    path("listar/",views.listar_movimiento,name='listar'),

]
