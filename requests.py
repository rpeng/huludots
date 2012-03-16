import os

import memcached
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

class NewGameRequest(TemplateRequest):
    def get(self):
        self.write("hello world")
