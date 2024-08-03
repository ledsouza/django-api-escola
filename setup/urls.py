from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from escola.views import (EstudanteViewSet, CursoViewSet,
                          MatriculaViewSet, ListaMatriculaEstudante, ListaMatriculaCurso)


router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, 'Estudantes')
router.register('cursos', CursoViewSet, 'Cursos')
router.register('matriculas', MatriculaViewSet, 'Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas', ListaMatriculaEstudante.as_view()),
    path('cursos/<int:pk>/matriculas', ListaMatriculaCurso.as_view()),
]
