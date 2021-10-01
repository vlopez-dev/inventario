from django.db.models import fields
from django import forms
from .models import Articulo


class ArticuloForm(forms.ModelForm):

    class Meta:
        model=Articulo
        fields = '__all__'
        
        labels = {
            'Nombre':'Nombre',
        }