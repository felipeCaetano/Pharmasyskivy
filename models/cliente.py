from sqlalchemy import Column, Integer, String

from infrastructure.core import *


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
    _observers = []

    def __repr__(self):
        return f'Cliente: {self.cpf} | {self.nome} {self.sobrenome}'

    def __getitem__(self, item):
        return getattr(self, item.lower())

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def add(self):
        print('salvei no banco')
        self.notify_all()

    def notify_all(self):
        for x in self._observers:
            x.model_is_changed()
