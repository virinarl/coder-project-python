from django.urls import path
from test_app.views import (form_new_course, formNewTeacher, saludo, saludar_a, 
                            mostrar_template, listar_cursos, listar_familiares, 
                            form_new_course, formNewTeacher, busquedaCamada, buscar)

urlpatterns = [
    path("saludar/", saludo),
    path("saludar/<nombre>",saludar_a),
    path("mi-template/", mostrar_template),
    path("cursos/", listar_cursos),
    path("familiares/", listar_familiares),
    path("nuevo_curso/", form_new_course),
    path("nuevo_profesor/", formNewTeacher),
    path("busquedaCamada/",busquedaCamada, name="BusquedaCamada"),
    path("buscar/", buscar)
]