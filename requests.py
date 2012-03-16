import os

import memcache
from tornado.template import Loader
from tornado.web import RequestHandler

import cfg


class TemplateRequest(RequestHandler):

    _template_path = os.path.join(cfg.root, 'templates')
    _loader = Loader(_template_path)

    def render_template(self, template, **kwargs):
        template = self._loader.load(template)
        rendered = template.generate(**kwargs)
        self.write(rendered)

class StartRequest(TemplateRequest):
    _mc = memcache.Client(['127.0.0.1:11211'])

    def _generate_id(self):
        return os.urandom(40).encode('base64').rstrip()

    def get(self):
        game_id = self._generate_id()
        self.write({
            'status':'ok',
            'game_token':game_id
        })


