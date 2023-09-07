from django.shortcuts import render,redirect,get_object_or_404
from .models import Reservas
from .forms import ReservasForm
# Create your views here.

def reserva_criar(request):
    if request.method =="POST":
        form = ReservasForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReservasForm()
    else:
        form = ReservasForm()

    return render(request,'reservas/form.html',{'form':form})
    


def reserva_editar(request,id):
    reserva = get_object_or_404(Reservas, id=id)
    if request.method == "POST":
        form = ReservasForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reserva_listar')
    else:
        form = ReservasForm(instance=reserva)
    
    return render (request,'reservas/form.html',{'form':form})


def reserva_listar(request):
    reservas = Reservas.objects.all()
    context = {
        'reservas':reservas
    }
    return render(request, 'reservas/reservas.html',context)

def reserva_remover(request,id):
    reserva = get_object_or_404(Reservas, id=id)
    reserva.delete()
    return redirect('reserva_listar')


    
    

