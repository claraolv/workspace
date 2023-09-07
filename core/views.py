from django.shortcuts import render,redirect,get_object_or_404
from reservas.models import Reservas
# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def detalhe_reserva(request,id):
    reservas=get_object_or_404(Reservas,id=id)
    context={
        'reservas':reservas
    }
    return render(request, 'core/detalhe.html', context)