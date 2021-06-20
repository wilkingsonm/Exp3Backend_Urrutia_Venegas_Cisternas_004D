from django.shortcuts import render, redirect
from .models import Vehiculo

# Create your views here.
def home(request):
    nombre = 'Jorge Venegas'
    
    vehiculos = Vehiculo.objects.all()  #similar al comando select

    return render(request, 'home.html', context={'nom_usuario': nombre, 'datos': vehiculos},
    )

def index(request):

    return render(request, 'index.html',
    )


def galeria(request):

    return render(request, 'GaleriaFotos.html',
    )

def registro(request):

    return render(request, 'Registros.html',
    )
