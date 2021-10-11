from django.db.models import fields
from django import forms
from .models import Movimiento

class MovimientoForm(forms.ModelForm):

    class Meta:
        model=Movimiento
        fields = '__all__'
        
        labels = {
            'Nombre':'Nombre',
            
        }