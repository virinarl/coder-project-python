from django.shortcuts import render

# Create your views here.
def mostrar_home(request):
    return render(request,"ContentApp/home.html", {})

def mostrar_profile(request):
    return render(request,"ContentApp/profile.html", {})