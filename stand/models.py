from django.db import models

# Create your models here.
class Stand(models.Model):
    localização = models.CharField(max_length=150)
    valor = models.FloatField()
    