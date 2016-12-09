#!/usr/bin/env python
# encoding=utf8
#!/usr/bin/env python
from views.base import BaseView
from core.logic import Group


class JoinView(BaseView):
    def post(self, group_id):
        me = self.get_current_user()
        group = Group(group_id)

        message = u'加入失败，请重试！'
        if group.join(me) == True:
            message = u'加入小组%s成功'%group.title

        self.message(message, '/')
