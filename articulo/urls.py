from django.urls import path
from . import views

urlpatterns = [
    # path("",), #Localhost:p/empresa/agregar
    path("agregar/",views.articulo_agregar,name='agregar'),
    path("listar/",views.listar_articulo,name='listar'),

]
