from sqlalchemy import Column, Boolean, Integer, String, Float
from sqlalchemy.orm.exc import NoResultFound

from infrastructure.core import *


def conect_db():
    return session


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
    _observers = []

    def __repr__(self):
        return f'{self.codigo} {self.nome} {self.p_ativo}' \
                f'{self.apresentacao} {self.dosagem} {self.preco} ' \
               f' {self.estoque}'

    def __getitem__(self, item):
        return getattr(self, item.lower())

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_all(self):
        for x in self._observers:
            x.model_is_changed()

    def add(self):
        print('salvei no banco')
        self.notify_all()

    def find_byid(self, idnum):
        session = conect_db()
        record = session.query(Medicamento).filter_by(id_client=idnum).one()
        session.close()
        return record

    def get_all(self):
        """
        faz a busca de toda uma tabela
        :return: registros de uma tabela
        """
        session = conect_db()
        record = session.query(Medicamento).all()
        session.close()
        return record

    def find_record(self, text, nome=""):
        """
        encontra um registro especifico da tabela usando o keyword
        :param text:
        :param nome: parametro a ser pesquisado
        :return: um registro da tabela
        """
        session = conect_db()
        try:
            result = session.query(Medicamento).filter(
                Medicamento.nome == text).one()
            session.close()
            return True, result
        except NoResultFound:
            session.close()
            return False, 'NOT_REGISTERED'


create_all()
