from django.shortcuts import render,redirect
from .forms import RegistroForm
from django.contrib import messages


from django.contrib.auth import login
from django.contrib.auth import logout
from django.views.generic import View

from registration import forms


# Create your views here.









def register_request(request):
	if request.method == "POST":
		form = RegistroForm(request.POST)
		if form.is_valid():
			print("Estoy en la validacion del form")
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegistroForm()
	return render (request=request, template_name="registration/registro.html", context={"RegistroForm":form})











class LoginPageView(View):
    template_name = 'registration/login.html'
    form_class = forms.LoginForm
    

def logout_view(request):
    logout(request)
    print("entre funcion logout")
    return redirect('/accounts/logout')



