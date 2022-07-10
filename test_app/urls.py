from django.urls import path
from test_app.views import saludo, saludar_a, mostrar_template, listar_cursos, listar_familiares

urlpatterns = [
    path("saludar/", saludo),
    path("saludar/<nombre>",saludar_a),
    path("mi-template/", mostrar_template),
    path("cursos/", listar_cursos),
    path("familiares/", listar_familiares),
]