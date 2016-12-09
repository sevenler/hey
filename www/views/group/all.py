#!/usr/bin/env python
# encoding=utf8
from views.base import BaseView
from core.logic import Group


class AllView(BaseView):
    def get(self):
        all_group_obj = Group.filter()
        group_map_list = []
        for group in all_group_obj:
            group_map_list.append(group.info())
        self.render("group/all.html", groups=group_map_list)
