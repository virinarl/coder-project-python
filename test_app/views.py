from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from test_app.models import Curso, Familiares
# Create your views here.

def saludo(request):
    return HttpResponse("Hola Mundo!")

def saludar_a(request, nombre):
    rightNow = datetime.now().strftime("%H:%M:%S") #Hora:minuto:segundos
    return HttpResponse(f"Hola, {nombre.capitalize()}! Son las {rightNow}")


def mostrar_template(request):
    context = {}
    
    if request.GET:
        context["nombre"] = request.GET["nombre"]
        
    return render(request, "test_app/index.html", context )

def listar_cursos(request):
    context={}
    
    context["cursos"] = Curso.objects.all()
    return render(request, "test_app/lista_cursos.html", context)

def listar_familiares(request):
    context={}
    
    context["familiares"] = Familiares.objects.all()
    return render(request, "test_app/familiares.html", context)
    
        