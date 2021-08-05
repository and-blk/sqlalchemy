from db import Base, session
from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import ProgrammingError


class ParentTable:
    def write(self):
        session.add(self)
        session.commit()
        return f'insert {self} to {self.__tablename__}'

    def __repr__(self):
        return f'{self.data}'

    def delete(self):
        discovered = self.find_by_name(self.data['name'])
        if discovered:
            session.delete()
            session.commit()
            return f'delete {self} from {self.__tablename__}'
        return f'no {self} to delete in {self.__tablename__}'

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(name=name).first()


class InfoTable(Base, ParentTable):
    __tablename__ = 'info'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)

    def __init__(self, data):
        self.data = data
        self.name = data['name']


class DataTable(Base, ParentTable):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    phone = Column(String(12))

    def __init__(self, data):
        self.data = data
        self.name = data['name']
        self.phone = data['phone']


def table_create(engine):
    Base.metadata.create_all(engine)
    print('tables have been created')


