from django.shortcuts import render,redirect
from .models import Area
from area.forms import AreaForm
from django.contrib import messages
import sweetify

# Create your views here.




def area_agregar(request,id_area=0):
    if request.method == "GET":
        if id_area == 0 :
            form = AreaForm()
        else:
            area = Area.objects.get(pk=id_area)

            form = AreaForm(instance=area)
        return render(request, 'area/area_agregar.html', {'form': form})
    else:
        if id_area == 0:
            form = AreaForm(request.POST)
        else:
            area = Area.objects.get(pk=id_area)
            form = AreaForm(request.POST,instance= area)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Exito', text='Agregado Correctamente', persistent='Aceptar')

        return redirect('/area/listar/')








def listar_area(request):
    context = {'listar_area': Area.objects.all()}
    return render(request, "area/listar.html", context)




def delete_area(request,id_area):
    area = Area.objects.get(pk=id_area)
    area.delete()
    return redirect('/area/listar/')
