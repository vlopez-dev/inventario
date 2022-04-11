from django.shortcuts import render,redirect
from .forms import RegistroForm
from django.contrib import messages


from django.contrib.auth import login
from django.contrib.auth import logout
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm #add this

from registration import forms


# Create your views here.









def registro_usuario(request):
	if request.method == "POST":
		form = RegistroForm(request.POST)
		print(" estoy por entrar a la validacion")
		if form.is_valid():
			form.cleaned_data.get('username')

			print("Estoy en la validacion del form")
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegistroForm()
	return render (request=request, template_name="registration/registro.html", context={"RegistroForm":form})











class LoginPageView(View):
    print("Entre por login")
    template_name = 'registration/login.html'
    form_class = forms.UserLoginForm
    
    

def logout_view(request):
    logout(request)
    print("entre funcion logout")
    return redirect('/accounts/logout')



