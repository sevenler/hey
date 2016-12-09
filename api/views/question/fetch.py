#!/usr/bin/env python
# encoding=utf8
from api.views.base import BaseApiView
from api.views.response import response


class FetchView(BaseApiView):
    def get(self):
        context = self.get_current_context()
        question_map_list = context.fetch_nearly_question()
        return response(self, question_map_list)
