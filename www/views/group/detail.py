#!/usr/bin/env python
# encoding=utf8
from views.base import BaseView
from core.logic import Group, User


class DetailView(BaseView):
    def get(self, group_id):
        group_map = {}
        group_obj = Group(group_id)
        group_map.update(group_obj.info())

        partner_id_list = group_obj.partners()
        user_list = []
        for partner in partner_id_list:
            for user in User.filter(id=partner['user_id']):
                user_list.append(user.info())
        group_map.update({
            'partners': user_list,
        })
        self.render("group/detail.html",group=group_map)
