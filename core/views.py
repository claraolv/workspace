from django.shortcuts import render,redirect,get_object_or_404
from reservas.models import Reservas
from django.views import generic

class HomeView(generic.TemplateView):
    template_name = "core/index.html"

class ReservaDetailView(generic.DetailView):
    model = Reservas
    template_name = "core/detalhe.html"
    
def detalhe_reserva(request,id):
    reservas=get_object_or_404(Reservas,id=id)
    context={
        'reservas':reservas
    }
    return render(request, 'core/detalhe.html',context)