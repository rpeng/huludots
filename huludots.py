import traceback
import logging

import tornado.web
import tornado.ioloop

from requests import *


def get_application():
    try:
        settings = {
            "debug": True
        }
        application = tornado.web.Application([
            (r'/start/?', NewGameRequest),
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
