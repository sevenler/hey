from core.logic.base import BaseObject
from core.models import Contact as ContactModel


class Contact(BaseObject):
    def __init__(self, pk):
        self._pk = pk

    @classmethod
    def create(cls, **kwargs):
        #me = kwargs['me']
        #contact_user_id = kwargs['contact_user_id']
        #text = kwargs['text']
        #image = kwargs['image']
        contact_model = ContactModel()
        return cls(contact_model.id, contact_model)
