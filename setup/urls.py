from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet


router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, 'Estudantes')
router.register('cursos', CursoViewSet, 'Cursos')
router.register('matriculas', MatriculaViewSet, 'Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
