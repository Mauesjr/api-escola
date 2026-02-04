from django.test import TestCase
from escola.models import Curso, Estudante


class FixturesTestcase(TestCase):
  fixtures = ['prototipo_banco.json']
  

  def test_cursos_carregados_dos_fixtures(self):
    """
    Teste para verificar se os cursos foram carregados corretamente dos fixtures.
    """
    estudante = Estudante.objects.get(cpf="78137664408")
    curso = Curso.objects.get(pk=1)
    self.assertEqual(estudante.nome, "Arthur")
    self.assertEqual(curso.descricao, "Python I")
