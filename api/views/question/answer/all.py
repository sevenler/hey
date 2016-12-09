#!/usr/bin/env python
# encoding=utf8
from api.views.base import BaseApiView
from api.views.response import response


class AllView(BaseApiView):
    def get(self, question_id):
        context = self.get_current_context()
        answer_map_list = context.fetch_answer(question_id=question_id)
        return response(self, answer_map_list)
