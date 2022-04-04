from django.shortcuts import render,redirect
from .forms import RegistroForm
from django.contrib import messages

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm 
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
	return render (request=request, template_name="registro/registro.html", context={"RegistroForm":form})







def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	
	return render(request=request, template_name="registro/login.html", context={"login_form":form})
	