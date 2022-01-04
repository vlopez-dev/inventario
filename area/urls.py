from django.urls import path
from . import views

urlpatterns = [
    path("agregar/",views.area_agregar,name='area_agregar'),
    path("listar/",views.listar_area,name='listar_area'),
    path('delete/<int:id_area>/',views.delete_area,name='area_delete'),
    path('<int:id_area>/', views.area_agregar,name='area_update'), # get and post req. for update operation


]
