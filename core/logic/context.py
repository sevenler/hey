from core.constant import DEFAULT_FETCH_QUESTION_WITH_USER_RANGE
from core.logic.question import Question
from core.logic.user import User
from core.models import session
from core.models import QuestionPrestorage as QuestionPrestorageModel


class Context(object):
    def __init__(self, user_id):
        self._user_id = user_id

    def fetch_nearly_question(self, **kwargs):
        return NearlyQuestionFetcher(user_id=self._user_id, **kwargs).fetch()

    def fetch_question(self, id=None):
        question_obj_list = Question.filter(id__in=[id])
        question_map_list = []
        for q in question_obj_list:
            question_map_list.append(q.info())
        return question_map_list

    def add_question(self, **kwargs):
        kwargs['created_user_id'] = self._user_id
        question_obj = Question.create(**kwargs)
        return question_obj.info()

    def add_answer(self, question_id, text=None, images=[]):
        answer_user_id = self._user_id
        question_obj = Question(question_id)
        question_obj.add_answer(answer_user_id, text, images)
        return True

    def fetch_answer(self, question_id):
        question_obj = Question(question_id)
        answer_obj_list = question_obj.filter_answer(question_id=question_id)
        return [obj.info() for obj in answer_obj_list]

    def __check_permit(self, question_obj):
        return question_obj.created_user_id == self._user_id

    def add_tags(self, question_id, add_user_id, tag_id_list=[]):
        question_obj = Question(question_id)
        if self.__check_permit(question_obj):
            question_obj.add_tags(add_user_id, tag_id_list)
        return True

    def enjoy_answer(self, answer_id):
        question_obj_list = Question.filter(answer_id=answer_id)
        if len(question_obj_list) == 0:
            raise Exception('answer id error')

        question_obj = question_obj_list[0]
        if self.__check_permit(question_obj):
            answer_obj = question_obj.enjoy_answer(answer_id)
            return answer_obj.info()


class NearlyQuestionFetcher(object):
    def __init__(self, user_id, **kwargs):
        self._user_id = user_id
        self._kwargs = kwargs

    def fetch(self, **kwargs):
        question_obj_list = self.__load_from_prestorage(**kwargs)
        self.__prestorage_question(**kwargs)
        return question_obj_list

    def __load_from_prestorage(self, **kwargs):
        prestorage_model_list = session.query(QuestionPrestorageModel).filter_by(user_id=self._user_id)
        question_id_list = []
        for prestorage_model in prestorage_model_list:
            question_id_list.append(prestorage_model.question_id)
            session.delete(prestorage_model)
        session.commit()

        question_obj_list = Question.filter(id__in=question_id_list)
        question_map_list = [q.info() for q in question_obj_list]
        return question_map_list

    def __prestorage_question(self, **kwargs):
        user_range_filter = self.__calculate_user_range(**kwargs)
        user_obj_list = User.filter(**user_range_filter)
        user_id_dict = set()
        for user_obj in user_obj_list:
            user_id_dict.add(user_obj.id)

        prestorage_max = kwargs.get('prestorage_max', 20)
        question_obj_list = Question.filter(created_user_id__in=user_id_dict)
        for index in range(0, min(prestorage_max, len(question_obj_list))):
            question_obj = question_obj_list[index]
            question_prestorage_model = QuestionPrestorageModel()
            question_prestorage_model.user_id = self._user_id
            question_prestorage_model.question_id = question_obj.id
            session.add(question_prestorage_model)
        session.commit()

    def __calculate_user_range(self):
        user_range = self._kwargs.get('user_range', DEFAULT_FETCH_QUESTION_WITH_USER_RANGE)
        user_obj = User(self._user_id)
        latitude_min = user_obj.latitude - user_range
        latitude_max = user_obj.latitude + user_range
        longitude_min = user_obj.longitude - user_range
        longitude_max = user_obj.longitude + user_range
        return {
            'latitude__min': latitude_min,
            'latitude__max': latitude_max,
            'longitude__min': longitude_min,
            'longitude__max': longitude_max,
        }
