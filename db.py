from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()
engine = create_engine(f'postgresql+psycopg2://{os.environ["PNAME"]}:{os.environ["PPASS"]}@{os.environ["PHOSTNAME"]}/{os.environ["DBNAME"]}')
Session = sessionmaker(engine)
session = Session()


def db_create(engine):
    if not database_exists(url=engine.url):
        create_database(url=engine.url)


if __name__ == '__main__':
    from tables import InfoTable, DataTable, table_create
    db_create(engine=engine)
    table_create(engine=engine)
    
    # list_variables = [{'name': 'mummy'}, {'name': 'mummy'}, 
    #                     {'name': 'daddy'}, {'name': 'grandf'},
    #                     {'name': 'grandm'}]
    list_variables = [{'name': 'mummy', 'phone': 534534}, {'name': 'mummy', 'phone': 534534}, 
                        {'name': 'daddy', 'phone': 22222}, {'name': 'grandf', 'phone': 00000},
                        {'name': 'grandm', 'phone': 2322312}]
    res = map(lambda x: DataTable(x).write(), list_variables)
    print(*list(res))

