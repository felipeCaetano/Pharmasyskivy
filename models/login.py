from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.exc import NoResultFound

from infrastructure.core import Base, create_all, session


def connect_db():
    return session


class Login(Base):
    """
    Classe para autenticar usuários com acesso ao sistema
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, index=True)
    password = Column(String)

    def __init__(self):
        self._observers = []

    def __repr__(self):
        return f'User: {self.nome}'

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
        session = connect_db()
        record = session.query(Login).filter_by(
            id_client=idnum).one()
        session.close()
        return record

    def get_all(self):
        """
        faz a busca de toda uma tabela
        :return: registros de uma tabela
        """
        session = connect_db()
        record = session.query(Login).all()
        session.close()
        return record

    def find_record(self, text):
        """
        encontra um registro especifico da tabela usando o keyword
        :param text:
        :param nome: parametro a ser pesquisado
        :return: um registro da tabela
        """
        session = connect_db()
        try:
            result = session.query(Login).filter(
                Login.nome == text).one()
            session.close()
            print(type(result))
            return True, result
        except NoResultFound:
            session.close()
            return False, 'NOT_REGISTERED'

    def validar_entrada(self, entrada):
        error = False
        msg = ''
        if not entrada:
            error = True
            msg = 'Campo Obrigatório'
        if entrada.isnumeric() or entrada.isspace():
            error = True
            msg = "formato inválido"
        elif entrada.isalpha():
            error = False
            msg = ''
        return error, msg

    def do_login(self, view):
        pass


create_all()

