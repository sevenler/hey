

from parse_post_body import ParsePostBodyMiddleware

def get_all_middleware():
    return [ParsePostBodyMiddleware()]
