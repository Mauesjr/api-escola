from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class CursoTestCase(TestCase):
  def setUp(self):
    self.usuario = User.objects.create_superuser(
      username="admin",password="admin123")
    self.url = reverse('Curso-list')
    self.client.force_authenticate(user=self.usuario)

