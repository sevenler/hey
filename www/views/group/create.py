#!/usr/bin/env python
# encoding=utf8
from views.base import BaseView
from core.logic import Group


class CreateView(BaseView):
    def get(self):
        self.render("group/create.html",)

    def post(self):
        title = self.get_argument('title', None)
        description = self.get_argument('description', None)
        max_partner_number = self.get_argument('max_partner_number', None)
        created_user = self.get_current_user()
        group_dict = {
            'title': title,
            'description': description,
            'max_partner_number': max_partner_number,
            'created_user_id': created_user.id,
        }
        group_obj = Group.create(**group_dict)
        message = u'创建小组%s成功！'%group_obj.info()['title']
        self.message(message, '/')
