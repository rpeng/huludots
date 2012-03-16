import traceback
import logging
import os

import tornado.web
import tornado.ioloop

from requests import *
import cfg


def get_application():
    try:
        settings = {
            "static_path": os.path.join(cfg.root, "static"),
            "debug": True
        }
        application = tornado.web.Application([
            (r'/game/(.+)/', GamePage),
            (r'/game/(.+)/move/', MoveRequest),
            (r'/?', StartRequest),
        ], **settings)

        return application

    except Exception, e:
        logging.error("Error: %s" % traceback.format_exc())
        raise e

application = get_application()

if __name__ == "__main__":
    application = get_application()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
