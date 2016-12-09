#!/usr/bin/env python
# encoding=utf8
from views.base import BaseView
from core.logic import Group


class MineView(BaseView):
    def get(self):
        me = self.get_current_user()

        my_group_list = Group.filter(created_user_id=me.id)
        group_map_list = []
        for group in my_group_list:
            group_map_list.append(group.info())
        self.render("group/mine.html", groups=group_map_list)
