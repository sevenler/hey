from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey
)

from base import BaseModel

class Question(BaseModel):
    __tablename__ = 'question'

    created_user_id = Column(Integer(), ForeignKey('user.id'), nullable=False)
    text = Column(Text())
    image = Column(String(1000))
