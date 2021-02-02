from sqlalchemy import Column, Integer, String, Float

from infrastructure.core import *


class Produto(Base):
    __tablename__ = 'produtos'
    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(Integer, nullable=False, unique=True)
    nome = Column(String, nullable=False, index=True)
    descricao = Column(String, nullable=False)
    quantidade = Column(String, nullable=False)
    unidadequantidade = Column(String, nullable=False)
    estoque = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    compra = Column(Float, nullable=False)
    validade = Column(String, nullable=False)
    tipo = Column(String, nullable=False)

    def __repr__(self):
        return f'{self.codigo} {self.nome}  {self.estoque} {self.preco}'


create_all()
