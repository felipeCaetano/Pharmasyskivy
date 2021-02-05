from sqlalchemy import Column, Integer, String, Date

from infrastructure.core import *


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, index=True)
    password = Column(String)

    def __repr__(self):
        return f'User: {self.nome}'


class Cliente(Base):
    __tablename__ = 'clientes'

    id_client = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(String(12), nullable=False, unique=True)
    nome = Column(String(50), nullable=False, index=True)
    sobrenome = Column(String(50), nullable=False)
    email = Column(String(140), nullable=False)
    telefone = Column(String(11))
    nascimento = Column(String, nullable=False)
    sexo = Column(String(1), nullable=False)

    def __repr__(self):
        return f'Cliente: {self.cpf} | {self.nome} {self.sobrenome}'

    def __getitem__(self, item):
        return getattr(self, item.lower())

    def __setitem__(self, key, value):
        return setattr(self, key, value)


class Funcionario(Base):
    __tablename__ = 'funcionarios'
    id_funcionario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False, index=True)
    sobrenome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefone = Column(String)
    data_nasc = Column(Date, nullable=False)
    sexo = Column(String(1), nullable=False)
    cpf = Column(String(12), nullable=False)
    funcao = Column(String, nullable=False)
    crf = Column(Integer)
    id_user = Column(Integer)


create_all()
