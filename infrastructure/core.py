"""modulo ´para conexao com o banco de dados."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///../infrastructure/banco.sqlite', echo=True)
# engine = create_engine(
# 'postgresql://postgres:dcaetanos@localhost/pharmabase', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()


def create_all():
    Base.metadata.create_all(engine)
