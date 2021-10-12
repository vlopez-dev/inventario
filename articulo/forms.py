from django.db import models
from django.db.models import fields
from django import forms
from .models import Articulo, Movimiento


class ArticuloForm(forms.ModelForm):

    class Meta:
        model=Articulo
        fields = '__all__'
        
      
      
      
class MovimientoForm(forms.ModelForm):

    class Meta:
        model=Movimiento
        fields = '__all__'
        
      