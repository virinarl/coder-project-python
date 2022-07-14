from socket import fromshare
from django import forms

class CursoFormulario(forms.Form):
    #Campos del formulario
    curso = forms.CharField()
    camada = forms.IntegerField()
    
class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField(label = "Correo Electrónico", required= True)
    profesion = forms.CharField()
    
    