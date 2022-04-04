from cProfile import label
from django.db.models import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm #add this


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    print("Estoy en el registro form")

    class Meta:
        model=User
        fields = ['username', 'email', 'password1','password2']
        labels = {
                'username':'Nombre de usuario','password':'Contraseña','password2':'Confirmación contraseña'

                }
    def save(self, commit=True):
            print("Estoy en el save")
            user = super(RegistroForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user






class CustomAuthenticationForm(AuthenticationForm):
     class Meta:
        model = User
        fields = '__all__'
       
        
     def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
     label={
            'Username':'Usuario'
        }