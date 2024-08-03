from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from escola.models import Estudante, Curso, Matricula
from escola.serializers import (EstudanteSerializer, CursoSerializer, MatriculaSerializer,
                                ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer)


class AuthenticatedViewMixin:
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class EstudanteViewSet(AuthenticatedViewMixin, viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer


class CursoViewSet(AuthenticatedViewMixin, viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(AuthenticatedViewMixin, viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculaEstudante(AuthenticatedViewMixin, generics.ListAPIView):

    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer


class ListaMatriculaCurso(AuthenticatedViewMixin, generics.ListAPIView):

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer
