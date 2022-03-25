from django.shortcuts import render,redirect
from .forms import RegistroForm
from django.contrib import messages


from django.contrib.auth import login
from django.contrib.auth import logout
from django.views.generic import View

from registration import forms


# Create your views here.








def registro_usuario(request):
	if request.method == "POST":
		form = RegistroForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registro exitoso." )
			return redirect("/home")
		messages.error(request, "No se registro el usuario, informacion no valida.")
	form = RegistroForm()
	return render (request=request, template_name="registration/registro.html", context={"RegistroForm":form})





class LoginPageView(View):
    template_name = 'registration/login.html'
    form_class = forms.LoginForm
    

def logout_view(request):
    logout(request)
    print("entre funcion logout")
    return redirect('/accounts/logout')



