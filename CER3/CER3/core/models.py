from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Residencia(models.Model):
    dueño = models.CharField(max_length=50)
    telefono = models.IntegerField()
    ID = models.IntegerField(primary_key=True)
    
    def __str__(self) -> str:
        return "Residencia "+ str(self.ID)

class Correspondencia(models.Model):
    remitente = models.CharField(max_length=50)
    norecibe = 'No'
    recibe = 'Si'
    recibido = [(norecibe, 'No Recibido'), (recibe, 'Recibido')] 
    estado = models.CharField(max_length=15, choices=recibido, default=norecibe,)
    destinatario = models.CharField(max_length=50)
    residencia = models.ForeignKey('Residencia', on_delete=models.SET_NULL, null=True)
    conserje = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="Conserje", limit_choices_to={'groups__name':"Conserje"})
    fecha = models.DateTimeField((""), auto_now=False, auto_now_add=False, default=now) #NO ENTREGADO
    
    def __str__(self) -> str:
        return "Correspondencia para " + str(self.destinatario)

