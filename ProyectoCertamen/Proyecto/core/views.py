from collections import UserList
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView 
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Equipo
from .models import Residencia
##### API
from core.serializers import EquipoSerializer
from rest_framework.viewsets import ModelViewSet
from core.models import Equipo

class EquipoApiViewSet(ModelViewSet):
    serializer_class = EquipoSerializer
    queryset = Equipo.objects.all()

def home(request):
    return render(request, "core/home.html")

def informe(request):
    EquipoLista = Equipo.objects.all()
    return render(request, "core/informe.html",{"Equipo": EquipoLista})







