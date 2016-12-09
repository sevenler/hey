from sqlalchemy import (
    Column,
    Integer,
)

from base import BaseModel

class QuestionPrestorage(BaseModel):
    __tablename__ = 'question_prestorage'

    user_id = Column(Integer())
    question_id = Column(Integer())
