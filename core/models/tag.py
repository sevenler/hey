from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from base import BaseModel

class Tag(BaseModel):
    __tablename__ = 'tag'

    name = Column(String(500))

class TagQuestionRel(BaseModel):
    __tablename__ = 'tag_question_rel'

    question_id = Column(Integer(), ForeignKey('question.id'), nullable=False)
    tag_id = Column(Integer(), ForeignKey('tag.id'), nullable=False)

