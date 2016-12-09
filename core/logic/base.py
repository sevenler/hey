class BaseObject(object):
    def __init__(self, pk):
        self._pk = pk

    @property
    def id(self):
        return self._pk

    def info(self):
        return {
            'id': self._pk
        }

    @classmethod
    def create(cls, **kwargs):
        pass

    @classmethod
    def filter(cls, **kwargs):
        pass
