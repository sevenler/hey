from tornado.web import url
from api.views import user, question
from api.views.question import answer

handlers = [
    url(r"/user/(?P<user_id>\w+)", user.DetailView, name='user.detail'),
    url(r"/user/(?P<user_id>\w+)/change/password/", user.ChangePasswordView, name='user.change_password'),
    url(r"/account/sign/up/", user.SignUpView, name='user.sign_up'),
    url(r"/account/sign/in/", user.SignInView, name='user.sign_in'),

    url(r"/question/nearly/", question.NearlyView, name='question.list'),
    url(r"/question/(?P<question_id>\w+)", question.DetailView, name='question.detail'),
    url(r"/question/add/", question.AddView, name='question.add'),

    url(r"/question/(?P<question_id>\w+)/answer/", answer.AllView, name='question.answer.list'),
    url(r"/question/(?P<question_id>\w+)/answer/add/", answer.AddView, name='question.answer.add'),
    url(r"/answer/(?P<answer_id>\w+)/agree/", answer.AgreeView, name='question.answer.agree'),
]
