from .forms import EmpresaForm
from django.db import models

from django.shortcuts import render,redirect

# Create your views here.



def empresa_agregar(request):
    if request.method=="GET":
        form =EmpresaForm()
    
        return render(request,'empresa/empresa_form.html',{'form':form})

    else:
        form =EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('empresa/empresa_list.html')
    



def listar_empresa(request):
    return render(request,'empresa/empresa_list.html')





