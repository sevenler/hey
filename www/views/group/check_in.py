#!/usr/bin/env python
# encoding=utf8
from views.base import BaseView
from core.logic import Group


class CheckInView(BaseView):
    def post(self, group_id):
        group_obj = Group(group_id)
        me = self.get_current_user()
        group_obj.check_in(me)
        message = u'打卡成功！'
        self.message(message, '/')
