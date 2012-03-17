import os

from tornado.template import Loader
from tornado.web import RequestHandler

import cfg
from lib import session_maker
from models.DotsGame import create_new_game

class MoveRequest(RequestHandler):
    def post(self):
        print self.request.arguments

class TemplateRequest(RequestHandler):

    _template_path = os.path.join(cfg.root, 'templates')
    _loader = Loader(_template_path)

    def render_template(self, template, **kwargs):
        template = self._loader.load(template)
        rendered = template.generate(**kwargs)
        self.write(rendered)


class StartRequest(TemplateRequest):

    def _generate_id(self):
        return os.urandom(40).encode('base64').rstrip()

    def get(self):
        game_id = self._generate_id()
        session_maker.new_session(game_id)
        self.write({
            'status':'ok',
            'game_token':game_id
        })


class StartPage(TemplateRequest):
    def get(self):
        board = create_new_game()
        self.render_template('start.html', board=board)
