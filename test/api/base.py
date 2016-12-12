import json
from app import Application
from tornado.testing import AsyncHTTPTestCase

class TestBase(AsyncHTTPTestCase):
    def get_app(self):
        return Application()

    def fetch(self, path, **kwargs):
        if kwargs.__contains__('method'):
            method = kwargs['method']
            if method == 'POST':
                kwargs['headers'] = {
                    'Content-Type': 'application/json'
                }

        response = super(TestBase, self).fetch(path, **kwargs)
        return self.__parse_response(response)

    def __parse_response(self, response):
        response.data = json.loads(response.body)
        return response
