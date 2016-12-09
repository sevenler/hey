from core.logic.base import BaseObject
from core.models import session
from core.models import Answer as AnswerModel


class Answer(BaseObject):
    def __init__(self, pk=None, model=None):
        super(Answer, self).__init__(pk)
        self._model = model

    def _lazy_load_model(self):
        if self._model== None:
            self._model = AnswerModel.filter_by(session=session, id=self._pk).first()

    @property
    def answer_user_id(self):
        self._lazy_load_model()
        return self._model.answer_user_id

    @property
    def question_id(self):
        self._lazy_load_model()
        return self._model.question_id

    def info(self):
        self._lazy_load_model()
        model = self._model
        info = {
            'text': model.text,
            'images': [model.image],
            'answer_user_id': model.answer_user_id,
        }
        info.update(super(Answer, self).info())
        return info

    def enjoy(self):
        self._lazy_load_model()
        self._model.is_enjoyed = True
        session.add(self._model)
        session.commit()

    @classmethod
    def create(cls, **kwargs):
        answer_model = AnswerModel()
        answer_model.answer_user_id = kwargs['answer_user_id']
        answer_model.question_id = kwargs['question_id']
        answer_model.text = kwargs['text']
        images = kwargs['images']
        if len(images) > 0:
            answer_model.image = images[0]

        session.add(answer_model)
        session.commit()

    @classmethod
    def filter(cls, **kwargs):
        answer_model_list = AnswerModel.filter_by(session=session, **kwargs).all()
        answer_object_list = []
        for item in answer_model_list:
            answer_object_list.append(cls(item.id, model=item))
        return answer_object_list
