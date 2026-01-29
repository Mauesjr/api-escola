from escola.models import Estudante, Curso, Matricula
from escola.serializer import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaEstudadeSerializer, ListaMatriculasCursoSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from escola.throtlhes import MatriculaAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import BaseThrottle

class EstudanteViewSet(viewsets.ModelViewSet):
  queryset = Estudante.objects.all().order_by("id")
  """
  Descrição da ViewSet:
  - Endpoint para CRUD de Estudantes

  Campos de Ordenação:
  - nome: Ordena pelo nome do estudante
  - data_nascimento: Ordena pela data de nascimento do estudante

  Campos de Busca:
  - nome: Busca pelo nome do estudante
  - cpf: Busca pelo CPF do estudante

  Métodos HTTP Permitidos:
  - GET, POST, PUT, PATCH, DELETE

  Classes de Serializador:
  - EstudanteSerializer: Usado para serialização e desserialização na versão padrão da API.
  - Se a versão da API for 'v2', usa EstudanteSerializerV2.
  """
  # serializer_class = EstudanteSerializer
  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  ordering_fields = ['nome', 'data_nascimento']
  search_fields = ['nome', 'cpf']
  def get_serializer_class(self):
    if self.request.version == 'v2':
      return EstudanteSerializerV2
    return EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
  """
  Docstring para ViewSet Curso:
  - Endpoint para CRUD de Cursos

  Métodos HTTP Permitidos:
  - GET, POST, PUT, PATCH, DELETE

  Campos de Busca:
  - descricao: Busca pela descrição (Nome) do curso.add()
  """

  queryset = Curso.objects.all().order_by("id")
  filter_backends = [DjangoFilterBackend, filters.SearchFilter]
  search_fields = ['descricao']
  serializer_class = CursoSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
  throttle_classes = []


class MatriculaViewSet(viewsets.ModelViewSet):
  """
  Docstring para ViewSet Matricula:
  - Endpoint para CRUD de Matrículas
  
  Métodos HTTP Permitidos:
  - GET, POST
  
  Trhotling Classes:
  - UserRateThrottle: Limita a taxa de requisições para usuários autenticados.
  - MatriculaAnonRateThrottle: Limita a taxa de requisições para usuários anônimos.
  """


  queryset = Matricula.objects.all().order_by("id")
  serializer_class = MatriculaSerializer
  throttle_classes = [UserRateThrottle,MatriculaAnonRateThrottle]
  http_method_names = ['get','post']


class ListaMatriculasEstudante(generics.ListAPIView):
  '''
  Descrição da View:
  - Lista Matriculas por id de Estudante
  Parâmetros:
  - pk (int): Id do Estudante

  '''

  def get_queryset(self):
    queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by("id")
    return queryset
  serializer_class = ListaMatriculaEstudadeSerializer

class ListaMatriculasCurso(generics.ListAPIView):
  """
  Descrição da View:
  - Lista Matriculas por id de Curso
  Parâmetros:
  - pk (int): Id do Curso
  """

  def get_queryset(self):
    queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by("id")
    return queryset
  serializer_class = ListaMatriculasCursoSerializer
  