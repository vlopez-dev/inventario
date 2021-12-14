from django.http import request
from django.shortcuts import render,redirect
from .models import Articulo, Movimiento
from articulo.forms import ArticuloForm, MovimientoForm
from django.contrib import messages
from django.db.models import Sum

# Create your views here.




def articulo_agregar(request,id_articulo=0):
    if request.method == "GET":
        if id_articulo == 0 :
            form = ArticuloForm()
        else:
            articulo = Articulo.objects.get(pk=id_articulo)
            #invernadero = Invernadero.objects.filter(pk=id_invernadero).first()

            form = ArticuloForm(instance=articulo)
        return render(request, 'articulo/articulo_agregar.html', {'form': form})
    else:
        if id_articulo == 0:
            form = ArticuloForm(request.POST)
        else:
            articulo = Articulo.objects.get(pk=id_articulo)
            form = ArticuloForm(request.POST,instance= articulo)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Agregado correctamente!.')

        return redirect('/articulo/listar_articulo/')



def movimiento(request,id_movimiento=0):
    if request.method == "GET":
        if id_movimiento == 0 :
            form = MovimientoForm()
        else:
            movimiento = Movimiento.objects.get(pk=id_movimiento)
            #invernadero = Invernadero.objects.filter(pk=id_invernadero).first()

            form = MovimientoForm(instance=movimiento)
        return render(request, 'articulo/movimiento_form.html', {'form': form})
    else:
        if id_movimiento == 0:
            form = MovimientoForm(request.POST)
        else:
            movimiento = Movimiento.objects.get(pk=id_movimiento)
            form = MovimientoForm(request.POST,instance= movimiento)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Agregado correctamente!.')

        return redirect('/articulo/listar_articulo/')











def listar_articulo(request):
    context = {'listar_articulo': Articulo.objects.all()}
    return render(request, "articulo/listar.html", context)




def delete_articulo(request,id_articulo):
    articulo = Articulo.objects.get(pk=id_articulo)
    articulo.delete()
    return redirect('/articulo/listar_articulo/')


def listar_movimientos(request):
    context = {'listar_movimientos':Movimiento.objects.all()}
    return render(request,"articulo/mover_list.html")



def delete_movimientos(request,id_movimiento):
    movimiento = Movimiento.objects.get(pk=id_movimiento)
    movimiento.delete()
    return redirect('/articulo/listar_articulo/')



def filtro_stock(request):
    cantidad_articulos= Movimiento.aggregate(Sum('cantidad_mover'))
