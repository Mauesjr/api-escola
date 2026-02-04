import re
from validate_docbr import CPF


def cpf_invalido(numero_cpf):
    cpf = CPF()
    return not cpf.validate(numero_cpf)

def nome_invalido(nome):
    # Permite letras (incluindo acentuadas) e espaços entre palavras
    nome = nome.strip()
    return not re.match(r'^[A-Za-zÀ-ÿ]+(?: [A-Za-zÀ-ÿ]+)*$', nome)

def numero_celular_invalido(numero_celular):
    # Modelo esperado: DDD 99999-9999
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return not resposta