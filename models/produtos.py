import re

from sqlalchemy import Column, Integer, String, Float, or_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound, UnmappedInstanceError

from infrastructure.core import *


def conect_db():
    return session


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
    _observers = []

    def __repr__(self):
        return f'{self.codigo} {self.nome}  {self.estoque} {self.preco}'

    def get_data(self):
        return [self.codigo, self.nome, self.descricao, self.preco,
                self.quantidade, self.estoque]

    def validate(self, text):
        if not text:
            error = True
            msg = 'Campo Obrigatório'
        elif text.isnumeric() or text.isspace():
            msg = "Formato Inválido"
            error = True
        elif text.isalpha():
            msg = 'Sucesso'
            error = False
        else:
            msg = 'Sucesso'
            error = False
        return error, msg

    def validate_number(self, text):
        if not text:
            error = True
            msg = 'Campo Obrigatório'
        elif text.isalpha() or text.isspace():
            msg = "Formato Inválido"
            error = True
        elif text.isdigit():
            msg = 'Sucesso'
            error = False
        else:
            msg = "Formato Inválido"
            error = True
        return error, msg

    def validate_price(self, price):
        error, msg, s = '', '', ''
        if not price:
            error = True
            msg = 'Campo Obrigatório'
        elif price.isalpha() or price.isspace():
            msg = "Formato Inválido"
            error = True
        elif price.isdigit() and float(price) > 0:
            msg = 'Sucesso'
            error = False
        pat = re.compile('[^0-9]')
        if '.' in price:
            s = re.sub(pat, '.', price)
        else:
            s = '.'.join(
                [re.sub(pat, '.', s) for s in price.split('.', 1)])
        return error, msg, s

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_all(self):
        for x in self._observers:
            x.model_is_changed()

    def add(self, fields):
        session = conect_db()
        session.add(fields)
        try:
            session.commit()
            session.close()
            self.notify_all()
            return True, 'Success'
        except UnmappedInstanceError:
            #return return_error(session, REGISTER_ERROR)
            print('UnmappedInstanceError')
        except IntegrityError:
            #return return_error(session, REGISTER_ERROR)
            print('IntegrityError')
        except Exception as e:
            print(e)

    def find_byid(self, idnum):
        session = conect_db()
        record = session.query(Produto).filter_by(id_client=idnum).one()
        session.close()
        return record

    def get_all(self):
        """
        faz a busca de toda uma tabela
        :return: registros de uma tabela
        """
        session = conect_db()
        record = session.query(Produto).all()
        session.close()
        return record

    def find_record(self, text):
        """
        encontra um registro especifico da tabela usando o keyword
        :param text:
        :param nome: parametro a ser pesquisado
        :return: um registro da tabela
        """
        session = conect_db()
        try:
            result = session.query(Produto).filter(
                or_(Produto.nome.contains(text),
                    Produto.descricao.contains(text),
                    Produto.codigo.contains(text))).all()
            session.close()
            return True, result
        except NoResultFound:
            session.close()
            return False, 'NOT_REGISTERED'


create_all()
