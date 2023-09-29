from django.urls import reverse_lazy
from django.views import generic
from reservas.models import Reservas
from .forms import ReservasForm
from django.contrib.messages import views

# Create your views here.

class ReservasListView(generic.ListView):
    model = Reservas
    paginate_by=2
    template_name = "reservas/reservas.html"

class ReservaCreateView(views.SuccessMessageMixin, generic.CreateView):
  model = Reservas
  form_class = ReservasForm
  success_url = reverse_lazy("reserva_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "reservas/form.html"
  
  
class ReservaDeleteView(generic.DeleteView):
  model = Reservas
  success_url = reverse_lazy("reserva_listar")
  template_name = "reservas/reservas_confirm_delete.html"
  
class ReservaUpdateView(views.SuccessMessageMixin,generic.UpdateView):
  model = Reservas
  form_class = ReservasForm
  success_url = reverse_lazy("reserva_listar")
  success_message= 'Alterações salvas!'
  template_name = "reservas/form.html"