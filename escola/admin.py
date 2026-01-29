from django.contrib import admin
from escola.models import Estudante, Curso, Matricula

class Estudantes(admin.ModelAdmin):
  list_display = ('id','nome', 'email', 'cpf', 'data_nascimento', 'numero_celular')
  search_fields = ('id','nome')
  list_display_links = ('id','nome')
  list_per_page = 10

    
admin.site.register(Estudante, Estudantes)

class Cursos(admin.ModelAdmin):
  list_display = ('id','codigo', 'descricao', 'nivel')
  search_fields = ('id','codigo')
  list_display_links = ('id','codigo')
  list_per_page = 10

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
  list_display = ('id','estudante', 'curso', 'periodo')
  search_fields = ('id','estudante__nome', 'curso__codigo')

admin.site.register(Matricula, Matriculas)