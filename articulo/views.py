from django.shortcuts import render,redirect
from .models import Articulo, Movimiento
from articulo.forms import ArticuloForm, MovimientoForm

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
    
    
    
def delete_articulo(request):
    articulo = Articulo.objects.get(pk=id)
    articulo.delete()
    return redirect('/articulo/list')



def listar_articulo(request):
    articulos = Articulo.objects.all()
    return render(request,'articulo/articulo_list.html',{'articulo':articulos})






def articulo_mover(request):
    if request.method=="GET":
        form =MovimientoForm()
    
        return render(request,'articulo/mover_form.html',{'form':form})

    else:
        form = MovimientoForm(request.POST)
        print(form)

        if form.is_valid():
            form.save()
        else:
            print("Error")
        return redirect('/articulo/listar/')
    
    
    
    
    
    
    

def listar_movimiento(request):
    movimiento = Movimiento.objects.all()
    return render(request,'articulo/mover_list.html',{'movimiento':movimiento})



