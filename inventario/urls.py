"""inventario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include,re_path
from registro import views as registro_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("registro/", registro_views.registro_usuario, name="registro"),
    path('registro/', include("registro.urls")),

    path('', include("empresa.urls")),
    path('area/', include("area.urls")),
    path('articulo/', include("articulo.urls")),


   re_path( r'^$',auth_views.LoginView.as_view(template_name="registro/login.html"), name="login"),
   re_path( r'^logout/$',auth_views.LoginView.as_view(template_name="registro/login.html"), name="logout"),


]
