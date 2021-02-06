from sqlalchemy import Column, Integer, String, Float, TIMESTAMP

from infrastructure.core import *


class Item(Base):
    __tablename__ = 'itens'
    id_item = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(Integer, nullable=False, unique=True)
    nome = Column(String, nullable=False, index=True)
    quantidade = Column(String, nullable=False)
    data = Column(TIMESTAMP, nullable=True)
    estoque = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    compra = Column(Float, nullable=False)
    validade = Column(String, nullable=False)
    valor = Column(String, nullable=False)
    tipo = Column(String, nullable=True)

    def __repr__(self):
        return f'{self.codigo}' \
               f'{self.nome}' \
               f'{self.quantidade}' \
               f'{self.estoque}' \
               f'{self.preco}'


class ItemVendido:
    def __init__(self, produto):
        self.codigo = produto.item.codigo
        self.nome = produto.item.nome
        self.quantidade = produto.txt_quantity.GetValue()
        self.data = None
        self.estoque = produto.item.estoque
        self.preco = produto.item.preco
        self.compra = produto.item.compra
        self.validade = produto.item.validade
        self.valor = produto.value
        self.tipo = None

    def __repr__(self):
        return f'{self.codigo} ' \
               f'{self.nome} ' \
               f'{self.quantidade} ' \
               f'{self.estoque} ' \
               f'{self.preco} ' \
               f'{self.valor} '


create_all()
