from django.shortcuts import render,redirect

from articulo.forms import ArticuloForm

# Create your views here.

def articulo_agregar(request):
    if request.method=="GET":
        form =ArticuloForm()
    
        return render(request,'articulo/articulo_form.html',{'form':form})

    else:
        form =ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('articulo/listar')
    



def listar_articulo(request):
    return render(request,'articulo/articulo_list.html')





