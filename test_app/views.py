import re
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from test_app.models import Curso, Familiares, Profesor
#Importo el formulario 
from test_app.forms import CursoFormulario, ProfesorFormulario 
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

def form_new_course(request):
    if request.method == "POST":
        #cargo la información del formulario en una variable
        miFormulario = CursoFormulario(request.POST)
        
        if miFormulario.is_valid(): #Verificar la válidez de los campos cargados en el form
            info = miFormulario.cleaned_data
            curso = Curso(nombre = info["curso"], camada = info["camada"])
            curso.save()
            #Vuelvo a la página de inicio
            return render(request, "test_app/index.html",{})
        
    else:
        miFormulario = CursoFormulario()
        
    return render(request, "test_app/formulario_nuevo_curso.html", {"miFormulario":miFormulario})

def formNewTeacher(request):
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            docente = Profesor(nombre=datos["nombre"], apellido=datos["apellido"], email=datos["email"], profesion=datos["profesion"])
            docente.save()
            return render(request, "test_app/index.html",{})
    
    else:
        formulario = ProfesorFormulario()
    
    return render(request, "test_app/formulario_profesor.html", {"miFormulario":formulario})

def busquedaCamada(request):
    return render(request, "test_app/busquedaCamada.html")

def buscar(request):
    if request.GET['camada']:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains = camada)
        
        return render(request,"test_app/resultadoBusqueda.html", {"cursos": cursos, "camada":camada})
    
    respuesta = "No enviaste datos"
    return HttpResponse(respuesta)
            
        