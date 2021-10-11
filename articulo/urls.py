from django.urls import path
from . import views

urlpatterns = [
    path("agregar/",views.articulo_agregar,name='agregar'),
    path("listar/",views.listar_articulo,name='listar'),

]
