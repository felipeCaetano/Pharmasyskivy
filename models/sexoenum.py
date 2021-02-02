from enum import Enum


class Sexo(Enum):
    notselect = 'Informe o Sexo'
    masculino = 'Masculino'.upper()
    feminino = 'Feminino'.upper()
    nenhum = 'Não informado'.upper()

    @classmethod
    def list_names(cls):
        lista = [member.value for member in cls]
        return lista
