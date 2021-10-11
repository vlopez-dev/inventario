from django.shortcuts import render,redirect
from .forms import MovimientoForm
from .models import Movimiento


# Create your views here.


def movimiento_agregar(request):
    if request.method=="GET":
        form =MovimientoForm()
    
        return render(request,'movimiento/movimiento_form.html',{'form':form})

    else:
        form =MovimientoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/movimiento/listar/')
    



def listar_movimiento(request):
    movimiento = Movimiento.objects.all()
    return render(request,'movimiento/movimiento_list.html',{'movimiento':movimiento})