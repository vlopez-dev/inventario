from django.http import request
from django.shortcuts import render,redirect
from .models import Articulo, Movimiento
from articulo.forms import ArticuloForm, FiltroStockForm, MovimientoForm
from django.contrib import messages
from django.db.models import Sum
from django.db.models import Avg
from django.db.models import Q
from itertools import chain




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



# def filtro_stock_total(request):
#     stockmovtotal=Movimiento.objects.all().aggregate(Sum('cantidad_mover'))
#     return render(request,"articulo/stock.html",stockmovtotal)


# def filtro_stock_area(request):
#     art_desechables = Articulo.objects.filter(desechable="True")
#     for i in  art_desechables:
#         articuloid=i.id_articulo
#     stock_area=Movimiento.objects.filter(id_articulo_id=articuloid,area_destino_id="2").aggregate(Sum('cantidad_mover'))
#     # queryset_2 = Movimiento.objects.filter(first_name__startswith='R') & User.objects.filter(last_name__startswith='D')
#     str(stock_area.quey)
#     return render(request,"articulo/stock.html",stock_area)

# def filtro_stock_area(request):
#    queryset = Articulo.objects.filter(Q(desechable=True)) & Movimiento.objects.filter(Q(area_origen='informatica'))
#    return render(request,"articulo/stock.html",{'articulos':queryset})









def filtro_stock_area(request):
    articulos = Articulo.objects.filter(desechable="True")
    movimientos = Movimiento.objects.filter(area_destino_id="2")
    articulos_list = (chain(articulos, movimientos))
    print(articulos_list)
      
    return render(request,"articulo/stock.html",{'articulos_list':articulos_list})




def filtro_stock(request):
     if request.method=="GET":
        form =FiltroStockForm()
        return render(request,'articulo/form_stock.html',{'form':form})
     else:
         form= FiltroStockForm(request.POST)
         if form.is_valid():
            area_origen = form.cleaned_data['area_origen']
            desechable = form.cleaned_data['desechable']
<<<<<<< HEAD
            print(area_origen)
            articulos = Articulo.objects.filter(desechable=True)
            movimientos = Movimiento.objects.filter(area_origen=area_origen)
            articulos_list = (chain(articulos, movimientos))

     return render(request, 'articulo/form_stock.html',{'articulos_list':articulos_list})
=======
            articulos = Articulo.objects.filter(desechable=desechable)
            # movimientos = Movimiento.objects.filter(area_destino_id=area_origen)
            movimientos=Movimiento.objects.filter(area_destino_id=area_origen).aggregate(Sum('cantidad_mover'))
            print(movimiento)
            articulos_list = (chain(articulos, movimientos))
            print(articulos_list)
            return render(request, 'articulo/stock.html',{'articulos_list':articulos_list})
>>>>>>> d61311519c7069a4d2a3894315b0a245b19c12fc
