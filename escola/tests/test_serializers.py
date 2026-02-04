from django.test import TestCase
from escola.models import Estudante
from escola.serializer import EstudanteSerializer

class SerializerEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome = "João Silva",
            email = "joao@gmail.com",
            cpf = "67877073127",
            data_nascimento = '2023-02-02',
            numero_celular = "11 99999-9999",
        )
        self.serializer = EstudanteSerializer(instance=self.estudante)
    def test_verifica_campos_serializados(self):
        """
        Docstring para teste de verificação dos campos serializados do estudante.
        """
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'nome', 'email', 'cpf', 'data_nascimento', 'numero_celular']))
        self.assertEqual(data['nome'], self.estudante.nome)
        self.assertEqual(data['email'], self.estudante.email)
        self.assertEqual(data['cpf'], self.estudante.cpf)
        self.assertEqual(data['data_nascimento'], str(self.estudante.data_nascimento))
        self.assertEqual(data['numero_celular'], self.estudante.numero_celular)
        