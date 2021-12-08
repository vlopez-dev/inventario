from .forms import EmpresaForm
from django.db import models
from .models import Empresa
from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    
    return render(request,'empresa/home.html')


def empresa_agregar(request):
    if request.method=="GET":
        form =EmpresaForm()
    
        return render(request,'empresa/empresa_form.html',{'form':form})


    else:
        form =EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/empresa/listar/')
    

def listar_empresa(request):
    empresas = Empresa.objects.all()
    return render(request,'empresa/empresa_list.html',{'empresa':empresas})




def delete_empresa(request,id_empresa):
    empresa = Empresa.objects.get(pk=id_empresa)
    empresa.delete()
    return redirect('/empresa_list')


