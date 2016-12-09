import json

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        return json.JSONEncoder.default(self, o)

def __response(handler, code, data=None, message=''):
    handler.set_status(code)
    handler.write(JSONEncoder().encode({
        'status': code,
        'data': data,
        'message': message,
    }))
    handler.finish()

def error_response(handler, code, message):
    __response(handler=handler, code=code, message=message)

def response(handler, data):
    __response(handler=handler, code=200, data=data)
