from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from base import BaseModel


class Answer(BaseModel):
    __tablename__ = 'answer'

    question_id = Column(Integer(), ForeignKey('question.id'), nullable=False)
    answer_user_id = Column(Integer(), ForeignKey('user.id'), nullable=False)
    answer_time = Column(DateTime())
    text = Column(Text())
    image = Column(String(1000))
    is_enjoyed = Column(Integer())
