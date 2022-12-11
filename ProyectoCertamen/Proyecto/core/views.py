from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView 
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Equipo
from .models import Residencia


def home(request):
    return render(request, "core/home.html")

def informe(request):
    EquipoLista = Equipo.objects.all()
    return render(request, "core/informe.html",{"Equipo": EquipoLista})





