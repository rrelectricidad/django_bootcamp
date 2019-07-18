from django.shortcuts import render
from django.http import HttpResponse

from pendientes.models import Tarea
from random import randint

# Create your views here.
    

def index(request):
    listita = Tarea.objects.all()
    persona = {"nombre":"dino",
     "edad":11,
     "altura":34,
     "hobbies":["futbol", "martillo", "caramelo", "nhokis"],
     "lista_tarea": listita 

     }
    return render(request, "inicio.html", persona)

     #retornamos el saludo

def tarea(request):
    saluda = "Hola,tarea /"
    return HttpResponse(saluda) #retornamos el saludo



