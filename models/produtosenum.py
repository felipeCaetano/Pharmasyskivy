from enum import Enum


class Produtos(Enum):
    nenhum = 'Escolha o tipo'.upper()
    perfum = 'Perfumaria'.upper()
    alim = 'Alimento'.upper()
    limp = 'Limpeza'.upper()
    outro = 'Outro'.upper()

    @classmethod
    def list_names(cls):
        lista = [member.value for member in cls]
        return lista
