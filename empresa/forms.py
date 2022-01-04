from django.db.models import fields
from django import forms
from .models import Empresa
class EmpresaForm(forms.ModelForm):

    class Meta:
        model=Empresa
        fields = '__all__'


        labels = {
                    'nombre':'Nombre','direccion':'Dirección','telefono':'Teléfono'

                }


    def __init__(self, *args, **kwargs):
        super(EmpresaForm,self).__init__(*args, **kwargs)
        # self.fields['position'].empty_label = "Select"
        self.fields['nombre'].required = False


# Falta definir que cambios deben estar en la modificacion