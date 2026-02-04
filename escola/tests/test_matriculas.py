from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Matricula, Estudante, Curso
from escola.serializer import MatriculaSerializer

class MatriculaTestCase(APITestCase):
  def setUp(self):
    self.usuario = User.objects.create_superuser(
      username="admin",password="admin123")
    self.url = reverse('Matricula-list')
    self.client.force_authenticate(user=self.usuario)
    
    # Criar estudante e curso primeiro
    self.estudante = Estudante.objects.create(
      nome="João Silva",
      cpf="12345678901",
      email="joao@silva.com",
      data_nascimento="2000-01-01",
      numero_celular="11 99999-9999"
    )
    
    self.curso = Curso.objects.create(
      codigo="PYTHON",
      descricao="Curso de Python",
      nivel="Básico"
    )
    
    self.matricula_01 = Matricula.objects.create(
      estudante=self.estudante,
      curso=self.curso,
      periodo="matutino",
    )
  def test_requisicao_para_listar_matriculas(self):
    """
    Teste de requisição para listar matrículas (GET).
    """
    response = self.client.get(self.url)#/matriculas/
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
  def test_requisicao_get_para_listar_uma_matricula(self):
    """
    Teste de requisição GET para listar uma matrícula específica.
    """
    response = self.client.get(self.url + f'{self.matricula_01.id}/')

    matricula_dados = Matricula.objects.get(pk=1)
    matricula_dados_serializados = MatriculaSerializer(instance=matricula_dados).data
    self.assertEqual(response.data, matricula_dados_serializados)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_requisicao_post_para_criar_uma_matricula(self):
    """
    Teste de requisição POST para criar uma matrícula.
    """
    dados_nova_matricula = {
      "estudante": self.estudante.id,
      "curso": self.curso.id,
      "periodo": "vespertino"
    }
    response = self.client.post(self.url, data=dados_nova_matricula)

    self.assertEqual(
      response.status_code,
      status.HTTP_201_CREATED
    )
