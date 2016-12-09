#!/usr/bin/env python
# encoding=utf8
from api.views.base import BaseApiView
from api.views.response import response


class AddView(BaseApiView):
    def post(self, question_id):
        text = self.request.data.get('text', '')
        images = self.request.data.get('images', [])
        context = self.get_current_context()
        data = context.add_answer(**{
            'question_id': question_id,
            'text': text,
            'images': images,
        })
        return response(self, data)
