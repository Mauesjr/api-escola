from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationTestCase(APITestCase):
  def setUp(self):
    self.usuario = User.objects.create_superuser(
      username="admin",password="admin123")
    self.url = reverse('Estudante-list')

    
  def test_autenticacao_usuario_com_credencias_validas(self):
    """
    Docstring para teste de autenticação de usuário com credenciais válidas.
    """
    usuario_autenticado = authenticate(
      username="admin", password="admin123")
    self.assertIsNotNone(usuario_autenticado)
    self.assertEqual(usuario_autenticado.username, self.usuario.username)

  def test_autenticacao_usuario_com_credencias_invalidas(self):
    """
    Docstring para teste de autenticação de usuário com credenciais inválidas.
    """
    usuario_autenticado = authenticate(
      username="admin", password="senha_incorreta")
    self.assertIsNone(usuario_autenticado)

  def test_requisicao_get_autorizada(self):
    """
    Docstring para teste de requisição GET autorizada.
    """
    self.client.force_authenticate(self.usuario)
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
