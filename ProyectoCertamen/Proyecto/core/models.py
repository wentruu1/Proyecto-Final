from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

DEPARTAMENT_CHOICES = (
    ("UCI", "UCI"),
    ("UTI", "UTI"),
)

  

# Create your models here.
class Residencia(models.Model):
    departamento = models.CharField(
        max_length = 20,
        choices = DEPARTAMENT_CHOICES,
        )
    ID = models.IntegerField(primary_key=True)
    
    def __str__(self) -> str: 
        return "Residencia "+ str(self.departamento)

class Equipo(models.Model):
    Codigo = models.IntegerField(primary_key=True)
    Marca = models.CharField(max_length=50)
    nomantencion = 'No'
    mantencion = 'Si'
    recibido = [(nomantencion, 'No Mantencion'), (mantencion, 'Mantencion')] 
    estado = models.CharField(max_length=15, choices=recibido, default=nomantencion,)
    modelo = models.CharField(max_length=50)
    residencia = models.ForeignKey('Residencia', on_delete=models.SET_NULL, null=True)
    matrona = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="matrona", limit_choices_to={'groups__name':"matrona"})
    fecha_mantencion = models.DateTimeField((""), auto_now=False, auto_now_add=False, default=now) 
    modelo = models.CharField(max_length=50)
    condicion = models.CharField(max_length=50)

    
    def __str__(self) -> str:
        return "Equipo " + str(self.Marca)

