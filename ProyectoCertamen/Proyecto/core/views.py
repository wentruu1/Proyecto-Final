from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Equipo
from .models import Residencia

# Create your views here.
#def home(request):
#    EquipoLista = Equipo.objects.all()    
#    return render(request, "core/home.html",{"Equipo": EquipoLista})

def home(request):
    return render(request, "core/home.html")

@login_required
def informe(request):
    EquipoLista = Equipo.objects.all()
    return render(request, "core/informe.html",{"Equipo": EquipoLista})

def autenticacion(request):
    if request.method == 'GET':
        return render(request, 'core/autenticacion.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'core/autenticacion.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('informe')
