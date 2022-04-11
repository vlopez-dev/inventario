from django.db.models.query import QuerySet
from django.http import request
from django.shortcuts import render,redirect
from .models import Articulo, Movimiento
from articulo.forms import ArticuloForm, FiltroStockForm, MovimientoForm
from django.contrib import messages
from django.db.models import Sum
from django.db.models import Avg
from django.db.models import Q
from itertools import chain
from django.shortcuts import get_object_or_404

import json





def articulo_agregar(request,id_articulo=0):
    if request.method == "GET":
        if id_articulo == 0 :
            form = ArticuloForm()
        else:
            articulo = Articulo.objects.get(pk=id_articulo)

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

        return redirect('/articulo/listar_movimientos/')











def listar_articulo(request):
    context = {'listar_articulo': Articulo.objects.all()}
    return render(request, "articulo/listar.html", context)




def delete_articulo(request,id_articulo):
    articulo = Articulo.objects.get(pk=id_articulo)
    articulo.delete()
    return redirect('/articulo/listar_articulo/')


def listar_movimientos(request):
    context = {'listar_movimientos':Movimiento.objects.all()}
    return render(request,"articulo/mover_list.html",context)



def delete_movimientos(request,id_movimiento):
    movimiento = Movimiento.objects.get(pk=id_movimiento)
    movimiento.delete()
    return redirect('/articulo/listar_movimientos/')




def filtro_stock(request):
     if request.method=="GET":
        form =FiltroStockForm()
        return render(request,'articulo/form_stock.html',{'form':form})
     else:
         form= FiltroStockForm(request.POST)
         if form.is_valid():
            area_destino = form.cleaned_data['area_destino']
            desechable = form.cleaned_data['desechable']
            articulos = Articulo.objects.filter(desechable=desechable)
            articulostotales=Articulo.objects.none()
            if not articulos:
                    return render(request, 'articulo/stock.html',{})
            else:
                for i in articulos:
                    movimientos = Movimiento.objects.filter(area_destino=area_destino,id_articulo_id=i.id_articulo)
                    if not movimientos:
                        return render(request, 'articulo/stock.html',{})
                    else:
                        total = movimientos.aggregate(Total=Sum('cantidad_mover'))
                        totalfinal=total.get('Total')

                        articulostotales|=articulos
                        qs = articulostotales.union(movimientos.select_related("id_articulo"))
                        print(qs.query)
                        articulos_list =  (chain(articulostotales, movimientos,total))

                        return render(request, 'articulo/stock.html',{'articulos_list':articulos_list,'totalfinal':totalfinal})



