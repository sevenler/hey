import tornado
from core.logic import User


class BaseView(tornado.web.RequestHandler):
    def get_current_user(self):
        #mock signed user
        user_id = 2
        if not user_id:
            return None

        user_obj_list = User.filter(id=user_id)
        if len(user_obj_list) > 0:
            return user_obj_list[0]
        else:
            return None

    def message(self, message='', redirect_to='/'):
        data = {'message': message, 'redirect_to': redirect_to}
        self.render("message.html", data=data)
