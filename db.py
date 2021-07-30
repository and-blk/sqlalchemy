from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('postgresql+psycopg2://postgres:pass@localhost/test_db')
Session = sessionmaker(engine)
session = Session()


def db_create(engine):
    if not database_exists(url=engine.url):
        create_database(url=engine.url)


def table_create(engine):
    Base.metadata.create_all(engine)
    print('tables have been created')


if __name__ == '__main__':
    from tables import InfoTable, DataTable
    db_create(engine=engine)
    table_create(engine=engine)
    list_variables = [{'name123': 'mummy', 'phone': 534534}, {'name': 'mummy', 'phone': 534534}, 
                        {'name': 'daddy', 'phone': 22222}, {'name': 'grandf', 'phone': 00000},
                        {'name': 'grandm', 'phone': 2322312}]
    # list_variables = [{'data': 'mummy', 'phone': 534534}, {'data': 'mummy', 'phone': 534534}, 
    #                     {'data': 'daddy', 'phone': 22222}, {'data': 'grandf', 'phone': 00000},
    #                     {'data': 'grandm', 'phone': 2322312}]
    res = map(lambda x: InfoTable(x).delete(), list_variables)
    print(*list(res))
    # print(base)
