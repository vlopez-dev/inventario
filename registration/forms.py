from django.db.models import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    print("Estoy en el registro form")

    class Meta:
        model=User
        fields = ['username', 'email', 'password1','password2']
        labels = {
                'username':'Nombre de usuario','password1':'Contraseña','password2':'Confirmación contraseña'

                }
    def save(self, commit=True):
            print("Estoy en el save")
            user = super(NewUserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user






class LoginForm():
    user = forms.CharField(required=True)

    class Meta:
        model=User
        fields = ['username', 'email', 'password1','password2']
        labels = {
                'username':'Nombre de usuario','password1':'Contraseña','password2':'Confirmación contraseña'

                }