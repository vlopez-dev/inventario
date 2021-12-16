from django.db import models
from django.db.models import fields
from django import forms

from area.models import Area
from .models import Articulo, Movimiento


class ArticuloForm(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = '__all__'


class MovimientoForm(forms.ModelForm):
    area_origen = forms.ModelChoiceField(queryset=Area.objects.all(), widget= forms.Select(attrs={'class':'form-control'}), )

    class Meta:
        model = Movimiento
        fields = '__all__'


class FiltroStockForm(forms.ModelForm):
    area_origen = forms.ModelChoiceField(queryset=Area.objects.all(), widget= forms.Select(attrs={'class':'form-control'}), )
    desechable = forms.BooleanField()
    class Meta:
        model = Movimiento
        fields = ['area_origen','desechable']
