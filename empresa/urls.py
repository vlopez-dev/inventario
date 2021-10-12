from django.urls import path
from . import views

urlpatterns = [
    # path("",), #Localhost:p/empresa/agregar
    path("agregar/",views.empresa_agregar,name='agregar'),
    path("listar/",views.listar_empresa,name='listar'),
    path("home/",views.home,name='home'),


]
