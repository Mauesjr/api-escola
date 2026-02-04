from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializer import EstudanteSerializer

class EstudanteTestCase(APITestCase):
  def setUp(self):
    self.usuario = User.objects.create_superuser(
      username="admin",password="admin123")
    self.url = reverse('Estudante-list')
    self.client.force_authenticate(user=self.usuario)
    self.estudante_01 = Estudante.objects.create(
      nome="Ana Silva",
      cpf="71746446439",
      email="ana@silva.com",
      data_nascimento="2000-05-15",
      numero_celular="11 99999-9999"
    )
    self.estudante_02 = Estudante.objects.create(
      nome="Bruno Souza",
      cpf="26871703489",
      email="bruno@souza.com",
      data_nascimento="1998-10-20",
      numero_celular="21 88888-8888"
    )

  def test_requisicao_para_listar_estudantes(self):
    """
    Teste de requisição para listar estudantes (GET).
    """
    response = self.client.get(self.url)#/estudantes/
    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  def test_requisicao_get_para_listar_um_estudante(self):
    """
    Teste de requisição GET para listar um estudante específico.
    """
    response = self.client.get(self.url + f'{self.estudante_01.id}/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    dados_estudantes = Estudante.objects.get(pk=1)
    dados_estudantes_serializers = EstudanteSerializer(instance=dados_estudantes).data
    self.assertEqual(response.data, dados_estudantes_serializers)
  
  def test_requisicao_post_para_criar_um_estudante(self):
    """
    Teste de requisição POST para criar um estudante.
    """
    dados_novo_estudante = {
      "nome":"Carla Mendes",
      "cpf":"11144477735",
      "email":"carla@mendes.com",
      "numero_celular":"31 77777-7777",
      "data_nascimento":"1995-07-30"
    }
    response = self.client.post(self.url, data=dados_novo_estudante)

    self.assertEqual(
      response.status_code,
      status.HTTP_201_CREATED
    )
    
  def test_requisicao_put_para_atualizar_um_estudante(self):
    """
    Teste de requisição PUT para atualizar um estudante.
    """
    dados_atualizados = {
      "nome":"Ana Paula Silva",
      "cpf":"71746446439",
      "email":"ana.paula@silva.com",
      "numero_celular":"11 98888-8888",
      "data_nascimento":"2000-05-15"
    }
    response = self.client.put(
      self.url + f'{self.estudante_01.id}/',
      data=dados_atualizados
    )
    
    self.assertEqual(
      response.status_code,
      status.HTTP_200_OK
    )
  
  def test_requisicao_delete_para_deletar_um_estudante(self):
    """
    Teste de requisição DELETE para deletar um estudante.
    """
    response = self.client.delete(
      self.url + f'{self.estudante_02.id}/'
    )
    
    self.assertEqual(
      response.status_code,
      status.HTTP_204_NO_CONTENT
    )
    