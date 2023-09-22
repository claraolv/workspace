from django.db import models
from stand.models import Stand
# Create your models here.
class Reservas(models.Model):
    cnpj = models.CharField(max_length=150)
    nome_empresa = models.CharField(max_length=150)
    categoria_empresa = models.CharField(max_length=150)
    quitado= models.BooleanField()
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE)
