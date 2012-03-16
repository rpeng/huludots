import random
import os

from tornado.template import Loader
from tornado.web import RequestHandler

import cfg
from lib import session_maker


class MoveRequest(RequestHandler):
    def post(self, game_token):
        self.write(game_token)

class TemplateRequest(RequestHandler):

    _template_path = os.path.join(cfg.root, 'templates')
    _loader = Loader(_template_path)

    def render_template(self, template, **kwargs):
        template = self._loader.load(template)
        rendered = template.generate(**kwargs)
        self.write(rendered)


class StartRequest(TemplateRequest):

    def _generate_id(self):
        bits = "%032x" % random.getrandbits(128)
        return bits

    def get(self):
        game_id = self._generate_id()
        session_maker.new_session(game_id)
        self.redirect('/game/' + game_id + '/')


class GamePage(TemplateRequest):

    def get(self, game_token):
        board = session_maker.load_session(str(game_token))
        self.render_template('game.html', board=board)
