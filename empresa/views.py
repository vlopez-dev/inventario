from articulo.models import Articulo, Movimiento
from .forms import EmpresaForm
from django.db import models
from .models import Empresa
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, 'empresa/home.html')




def empresa_agregar(request, id_empresa=0):
    if request.method == "GET":
        if id_empresa == 0:
            form = EmpresaForm()
        else:
            empresa = Empresa.objects.get(pk=id_empresa)
            #invernadero = Invernadero.objects.filter(pk=id_invernadero).first()

            form = EmpresaForm(instance=empresa)
        return render(request, 'empresa/empresa_agregar.html', {'form': form})
    else:
        if id_empresa == 0:
            form = EmpresaForm(request.POST)
        else:
            empresa = Empresa.objects.get(pk=id_empresa)
            form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO,
                                 'Agregado correctamente!.')

        return redirect('/listar/')


def listar_empresa(request):
    context = {'listar_empresa': Empresa.objects.all()}
    return render(request, "empresa/listar.html", context)


def delete_empresa(request, id_empresa):
    empresa = Empresa.objects.get(pk=id_empresa)
    empresa.delete()
    return redirect('/listar/')


def ultimos_movimientos(request):
        if request.user.is_authenticated:
            print("Es autenticado")
            movimientos = Movimiento.objects.all()
            articulos = Articulo.objects.all()

            return render(request, "empresa/home.html", {'movimientos':movimientos,'articulos':articulos})


        else:
                print("no es autenticado")
                return redirect('/accounts/login')
