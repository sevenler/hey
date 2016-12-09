#!/usr/bin/env python
# encoding=utf8
from api.views.base import BaseApiView
from api.views.response import response


class DetailView(BaseApiView):
    def get(self, question_id):
        context = self.get_current_context()
        include_answer = self.get_argument('answer', True)
        question_map_list = context.fetch_question(id=question_id)
        question_map = question_map_list[0]
        question_map['answers'] = context.fetch_answer(question_id=question_id)
        return response(self, question_map)
