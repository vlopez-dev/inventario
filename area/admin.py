from django.contrib import admin

from articulo.models import Movimiento
from .models import Area

# Register your models here.
admin.site.register(Area)
admin.site.register(Movimiento)

