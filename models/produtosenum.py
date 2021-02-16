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

    @classmethod
    def list_names_kivy(cls):
        lista = [{'text': member.value} for member in cls]
        return lista


class UnidadeVolume(Enum):
    unidade = 'Unidade dosagem:'
    litro = 'L'
    mililitro = 'mL'
    grama = 'g'
    miligrama = 'mg'
    kilograma = 'kg'
    micrograma = 'ug'
    tonelada = 't'
    microlitro = 'uL'

    @classmethod
    def list_names(cls):
        lista = [member.value for member in cls]
        return lista

    @classmethod
    def list_names_kivy(cls):
        lista = [{'text': member.value} for member in cls]
        return lista
