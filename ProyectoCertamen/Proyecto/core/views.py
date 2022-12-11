from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipo
from .models import Residencia

# Create your views here.
#def home(request):
#    EquipoLista = Equipo.objects.all()    
#    return render(request, "core/home.html",{"Equipo": EquipoLista})

def home(request):
    return render(request, "core/home.html")

def informe(request):
    EquipoLista = Equipo.objects.all()    
    return render(request, "core/informe.html",{"Equipo": EquipoLista})


