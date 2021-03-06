#!/usr/bin/env python
# encoding=utf8
from api.views.base import BaseApiView
from api.views.response import response


class DetailView(BaseApiView):
    def get(self, question_id):
        context = self.get_current_context()
        #include_answer = self.get_argument('answer', True)
        question_map_list = context.fetch_question(id=question_id)


        question_map = question_map_list[0]
        self._fetch_user_info(context, question_map, 'created_user_id', 'created_user')

        question_map['answers'] = context.fetch_answer(question_id=question_id)
        self._fetch_user_info(context, question_map['answers'], 'answer_user_id', 'answer_user')
        return response(self, question_map)

    def _fetch_user_info(self, context, ob, foreign_key, replaced_key):
        user_id_set = set()

        if type(ob) == dict:
            user_id_set.add(ob[foreign_key])
        elif type(ob) == list:
            for item in ob:
                user_id_set.add(item[foreign_key])
        else:
            raise Exception('error type')

        user_info_map = {item['id']:item for item in context.fetch_user(id__in=user_id_set)}
        if type(ob) == dict:
            ob[replaced_key] = user_info_map.get(ob[foreign_key], {})
            del ob[foreign_key]
        else:
            for q in ob:
                q[replaced_key] = user_info_map.get(q[foreign_key], {})
                del q[foreign_key]

        return ob
