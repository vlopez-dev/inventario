from django.urls import path

from . import views
from django.views.generic.base import TemplateView # new




urlpatterns = [
    # path("",), #Localhost:p/empresa/agregar
    path("registro/",views.registro_usuario,name='registro'),
    



]
