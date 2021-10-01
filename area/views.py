from django.shortcuts import render,redirect

from area.forms import AreaForm

# Create your views here.



def area_agregar(request):
    if request.method=="GET":
        form =AreaForm()
    
        return render(request,'area/area_form.html',{'form':form})

    else:
        form =AreaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('area/area_list.html')
    



def listar_area(request):
    return render(request,'area/area_list.html')
