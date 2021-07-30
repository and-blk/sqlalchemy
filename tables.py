import inspect
from db import Base, session
from sqlalchemy import Column, Integer, String


class ArgException(Exception):
    def __init__(self, args):
        self.args = args
        self.message = f'Wrong arguments {self.args}'

    def __str__(self):
        return f'{self.message}'


class ParentTable:
    
    def write(self):
        session.add(self)
        session.commit()
        return f'insert {self} to {self.__tablename__}'

    def __repr__(self):
        return f'{self.data}'

    def delete(self):
        discovered = self.find_by_query(self.data['name'])
        if discovered:
            session.delete()
            session.commit()
            return f'delete {self} from {self.__tablename__}'
        return f'no {self} to delete in {self.__tablename__}'

    @classmethod
    def find_by_query(cls, name):
        return session.query(cls).filter_by(name=name).first()

    def argument_checker(self, data):
        if not set(data) == set(self.__dict__.keys()):
            raise ArgException(data)


class InfoTable(Base, ParentTable):
    __tablename__ = 'info'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __init__(self, data):
        self.data = data
        self.argument_checker(data)
        self.name = data['name']


class DataTable(Base, ParentTable):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    data = Column(String(100))
    phone = Column(String(12))

    def __init__(self, data):
        self.data = data
        self.argument_checker(data)
        self.data = data['data']
        self.phone = data['phone']




