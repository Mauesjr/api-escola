from django.test import TestCase
from escola.models import Estudante

class ModelEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome="João Silva",
            email="joao@gmail.com",
            cpf="67877073127",
            data_nascimento='2023-02-02',
            numero_celular="11 99999-9999",
        )

    def test_verifica_atributos_de_estudante(self):
        """
        Docstring para teste de verificação de atributos do estudante.
        """
        self.assertEqual(self.estudante.nome, "João Silva")
        self.assertEqual(self.estudante.email, "joao@gmail.com")
        self.assertEqual(self.estudante.cpf, "67877073127")
        self.assertEqual(str(self.estudante.data_nascimento), '2023-02-02')
        self.assertEqual(self.estudante.numero_celular, "11 99999-9999")


