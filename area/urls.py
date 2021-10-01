from django.urls import path
from . import views

urlpatterns = [
    # path("",), #Localhost:p/empresa/agregar
    path("agregar/",views.area_agregar,name='agregar'),
    path("listar/",views.listar_area,name='listar'),

]
