from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def saludo(request):
    return HttpResponse("Hola Mundo!")

def saludar_a(request, nombre):
    rightNow = datetime.now().strftime("%H:%M:%S") #Hora:minuto:segundos
    return HttpResponse(f"Hola, {nombre.capitalize()}! Son las {rightNow}")


def mostrar_template(request):
    return render(request, "test_app/index.html")