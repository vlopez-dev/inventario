from django.db.models import fields
from django import forms
from .models import Area
class AreaForm(forms.ModelForm):

    class Meta:
        model=Area
        fields = '__all__'
        
        labels = {
             'Nombre':'Nombre',
        }