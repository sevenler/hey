#!/usr/bin/env python
# encoding=utf8
from core.logic.base import BaseObject
from core.models import session
from core.models import Question as QuestionModel
from core.models import TagQuestionRel as TagQuestionRelModel
from answer import Answer
from contact import Contact


class Question(BaseObject):
    def __init__(self, pk, model=None):
        super(Question, self).__init__(pk)
        self._model = model

    def _lazy_load_model(self):
        if self._model == None:
            self._model = QuestionModel(self._pk)

    def info(self):
        self._lazy_load_model()
        model = self._model
        info = {
            'text': model.text,
            'images': [model.image],
            'created_user_id': model.created_user_id,
        }
        info.update(super(Question, self).info())
        return info

    @property
    def created_user_id(self):
        self._lazy_load_model()
        return self._model.created_user_id

    def add_answer(self, answer_user_id, text=None, images=[]):
        return Answer.create(**{
            'answer_user_id': answer_user_id,
            'question_id': self._pk,
            'text': text,
            'images': images,
        })

    def filter_answer(self, **kwargs):
        kwargs['question_id'] = self._pk
        return Answer.filter(**kwargs)

    def enjoy_answer(self, answer_id):
        answer = Answer(answer_id)
        answer.enjoy()
        #self.__add_contact(answer.answer_user_id)
        return answer

    def __add_contact(self, answer_user_id):
        enjoy_user_id = self._model.created_user_id
        contact = Contact.create(me=enjoy_user_id, contact=answer_user_id)
        return contact

    def add_tags(self, add_user_id, tag_id_list=[]):
        for tag_id in tag_id_list:
            tag_question_rel_model = TagQuestionRelModel()
            tag_question_rel_model.add_user_id = add_user_id
            tag_question_rel_model.tag_id = tag_id
            tag_question_rel_model.question_id = question_id
            session.add(tag_question_rel_model)
        session.commit()

    @classmethod
    def filter(cls, **kwargs):
        kwargs = cls.__preprocess_answer_filter_arg(**kwargs)

        question_model_list = QuestionModel.filter_by(session=session, **kwargs).all()
        question_object_list = []
        for item in question_model_list:
            question_object_list.append(cls(item.id, model=item))
        return question_object_list

    @classmethod
    def __preprocess_answer_filter_arg(cls, **kwargs):
        if kwargs.__contains__('answer_id'):
            answer_id = kwargs.pop('answer_id')
            if len(kwargs) > 0:
                raise Exception('if query with answer_id, not support other argument')

            answer_list = Answer.filter(id=answer_id)
            if len(answer_list) > 0:
                question_id = answer_list[0].question_id
                kwargs['id'] = question_id
            else:
                kwargs['id'] = -1

        return kwargs

    @classmethod
    def create(cls, **kwargs):
        text = kwargs['text']
        images = kwargs['images']
        created_user_id = kwargs['created_user_id']

        question_model = QuestionModel()
        question_model.text = text
        question_model.created_user_id = created_user_id
        if len(images) > 0:
            question_model.image = images[0]

        session.add(question_model)
        session.commit()
        return cls(question_model.id, question_model)
