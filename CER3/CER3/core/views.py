from django.shortcuts import render
from django.http import HttpResponse
from .models import Correspondencia
from .models import Residencia

# Create your views here.
def home(request):
    CorrespondenciaLista = Correspondencia.objects.all()    
    return render(request, "core/conserjeria.html",{"Correspondencia": CorrespondenciaLista})


 #correspondencia = Correspondencia.objects.filter().order_by("residencia")
