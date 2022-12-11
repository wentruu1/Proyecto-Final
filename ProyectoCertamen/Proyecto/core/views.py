from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipo
from .models import Residencia

# Create your views here.
def home(request):
    EquipoLista = Equipo.objects.all()    
    return render(request, "core/conserjeria.html",{"Equipo": EquipoLista})


 #Equipo = Equipo.objects.filter().order_by("residencia")
