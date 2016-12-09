from base import BaseMiddleware
import json


class ParsePostBodyMiddleware(BaseMiddleware):
    def prepare_request(self, handler):
        self._parse_post_data(handler)

    def _parse_post_data(self, handler):
        if handler.request.method == 'POST':
            body = handler.request.body
            data = json.loads(body)
            handler.request.data = data
