from django.urls import path
from . import views

urlpatterns = [
    # path("",), #Localhost:p/empresa/agregar
    path("agregar/",views.empresa_agregar,name='empresa_agregar'),
    path('delete/<int:id_empresa>/',views.delete_empresa,name='empresa_delete'),
    path('<int:id_empresa>/', views.EmpresaForm,name='empresa_update'), # get and post req. for update operation

    path("listar/",views.listar_empresa,name='listar'),
    path("",views.home,name='home'),


]
