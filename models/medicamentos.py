from sqlalchemy import Column, Boolean, Integer, String, Float

from infrastructure.core import *


class Medicamento(Base):
    __tablename__ = 'medicamentos'
    id_medicamento = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(Integer, nullable=False, unique=True)
    nome = Column(String, nullable=False, index=True)
    p_ativo = Column(String, nullable=False, index=True)
    dosagem = Column(String, nullable=False)
    unidadedosagem = Column(String, nullable=False)
    classe = Column(String, nullable=False)
    laboratorio = Column(String, nullable=False)
    registroms = Column(String, nullable=False, unique=True)
    apresentacao = Column(String, nullable=False)
    tarja = Column(String, nullable=False)
    validade = Column(String, nullable=False)
    quantidade = Column(String, nullable=False)
    unidadequantidade = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    compra = Column(Float, nullable=False)
    estoque = Column(String, nullable=False)
    sngpc_control = Column(Boolean, nullable=False)

    def __repr__(self):
        return f'{self.codigo} {self.nome} {self.p_ativo} {self.apresentacao}' \
               f' {self.dosagem} {self.preco} {self.estoque} '

    def __getitem__(self, item):
        return getattr(self, item.lower())

    def __setitem__(self, key, value):
        return setattr(self, key, value)


create_all()
