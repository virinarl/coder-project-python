from django.urls import path
from ContentApp.views import mostrar_home, mostrar_profile

urlpatterns = [
    path("home/", mostrar_home, name="Home"),
    path("profile/",mostrar_profile, name="Profile"),
]