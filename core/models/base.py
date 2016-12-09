from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def install_model(engine):
    """Sync model into database, Invoked from application
    """
    Base.metadata.create_all(bind=engine)
    print "Models Installed"

class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    edited_time = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    created_time = Column(DateTime(), default=datetime.now)

    def __repr__(self):
        return '<%s: %d>' % (self.__class__.__name__, self.id)

    @property
    def json(self):
        raise NotImplementedError

    def update(self, update_dict):
        [setattr(self, key, value) for key, value in update_dict.iteritems()]

    @classmethod
    def filter_by(cls, session, **kwargs):
        model = cls
        query = session.query(model)
        for key, value in kwargs.items():
            pip = ExtraFilter(model, query, key, value)
            query = pip.filter()
        return query


class InFilter(object):
    def filter(self, model, query, key_real, key_type, value):
        key_call = getattr(model, key_real)
        return query.filter(key_call.in_(value))

class MinFilter(object):
    def filter(self, model, query, key_real, key_type, value):
        key_call = getattr(model, key_real)
        return query.filter(key_call >= value)

class MaxFilter(object):
    def filter(self, model, query, key_real, key_type, value):
        key_call = getattr(model, key_real)
        return query.filter(key_call <= value)

class UniversalFilter(object):
    def filter(self, model, query, key_real, key_type, value):
        return query.filter_by(**{key_real: value})

class ExtraFilter(object):
    SUPPORTED_FILTER = {
        'in': InFilter,
        'min': MinFilter,
        'max': MaxFilter,
        'universal': UniversalFilter,
    }

    def __init__(self, model, query, key, value):
        self._model = model
        self._query = query

        key_real = key
        key_type = 'universal'
        if '__' in key:
            keys = key.split('__')
            if len(keys) != 2:
                raise Exception('not support filtr arg: %s'%key)
            else:
                key_real = keys[0]
                key_type = keys[1]

        self._key_real = key_real
        self._key_type = key_type
        self._value = value

    def filter(self):
        FILTER_OBJECT = ExtraFilter.SUPPORTED_FILTER.get(self._key_type, None)
        if FILTER_OBJECT == None:
            raise Exception('not support filtr arg: %s'%self._key_type)
        return FILTER_OBJECT().filter(self._model, self._query, self._key_real, self._key_type, self._value)
