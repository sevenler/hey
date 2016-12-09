from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    ForeignKey
)

from base import BaseModel

class Contact(BaseModel):
    __tablename__ = 'contact'

    user_id = Column(Integer(), ForeignKey('user.id'), nullable=False)
    last_contact_time = Column(DateTime())
    last_contact_message = Column(Text())
