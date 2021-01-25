# from sqlalchemy.exc import IntegrityError
# from sqlalchemy.orm.exc import UnmappedInstanceError, NoResultFound
#
# from models import pessoas
# from models.pessoas import User
#
#
#
# def find_record(record, table):
#     """
#     encontra um registro especifico da tabela usando o keyword
#     :param cpf: coluna a ser pesquisada
#     :param nome: parametro a ser pesquisado
#     :return: um registro da tabela
#     """
#     session = conect_db()
#     try:
#         result = session.query(table).filter(table.nome == record[nome] and table.).one()
#         session.close()
#         return True, result
#     except NoResultFound:
#         session.close()
#         return False, NOT_REGISTERED
