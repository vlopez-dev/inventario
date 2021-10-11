from django.shortcuts import render,redirect
from .models import Articulo
from articulo.forms import ArticuloForm

# Create your views here.



def articulo_agregar(request):
    if request.method=="GET":
        form =ArticuloForm()
    
        return render(request,'articulo/articulo_form.html',{'form':form})

    else:
        form = ArticuloForm(request.POST)
        print(form)

        if form.is_valid():
            form.save()
        else:
            print("Error")
        return redirect('/articulo/listar/')
    



def listar_articulo(request):
    articulos = Articulo.objects.all()
    return render(request,'articulo/articulo_list.html',{'articulo':articulos})





