import tornado
from core.logic import User, Context
from api.middleware import get_all_middleware


class BaseApiView(tornado.web.RequestHandler):
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

    def get_current_context(self):
        user_obj = self.get_current_user()
        context = Context(user_obj.id)
        return context

    def prepare(self):
        for middleware in get_all_middleware():
            middleware.prepare_request(self)

#    def finish(self):
#        for middleware in get_all_middleware():
#            middleware.prepare_response(self)
