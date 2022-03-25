from django.urls import path

from . import views



urlpatterns = [
    # path("",), #Localhost:p/empresa/agregar
    path("registro_usuario/",views.registro_usuario,name='registro_usuario'),

    path("logout/",views.logout_view,name='logout'),
    path("login/",views.login,name='login'),
    

    

]
