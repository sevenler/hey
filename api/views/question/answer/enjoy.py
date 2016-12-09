#!/usr/bin/env python
# encoding=utf8
from api.views.base import BaseApiView
from api.views.response import response


class EnjoyView(BaseApiView):
    def post(self, answer_id):
        context = self.get_current_context()
        data = context.enjoy_answer(answer_id)
        return response(self, data)
