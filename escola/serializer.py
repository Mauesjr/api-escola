from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, numero_celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'numero_celular']
    
    def validate(self,dados):

        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF informado é inválido.'})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome deve conter apenas letras.'})
        if numero_celular_invalido(dados['numero_celular']) :
            raise serializers.ValidationError({'numero_celular':'O número de celular deve conter até 13 números e seguir o padrão: 86 99999-9999'})
        
        return dados

class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email','numero_celular']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class ListaMatriculaEstudadeSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self,obj):
        return obj.get_periodo_display()

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante']