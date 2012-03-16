import memcached
from tornado.web import RequestHandler


class NewGameRequest(RequestHandler):
    def get(self):
        self.write("hello world")
