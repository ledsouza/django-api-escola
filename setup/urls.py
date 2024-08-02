from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from escola.views import EstudanteViewSet, CursoViewSet


router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, 'Estudantes')
router.register('cursos', CursoViewSet, 'Cursos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
