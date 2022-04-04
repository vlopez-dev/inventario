from django.urls import path

from . import views



urlpatterns = [
    # path("",), #Localhost:p/empresa/agregar
    path("registro/",views.registro_usuario,name='registro'),



]
