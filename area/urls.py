from django.urls import path
from . import views

urlpatterns = [
    path("agregar/",views.area_agregar,name='area_agregar'),
    path("listar/",views.listar_area,name='area_listar'),

]
