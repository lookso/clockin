import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

from pymongo import MongoClient
from handlers import *

define("port", default=8000, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/api/login', LoginHandler),
            (r'/sys/health', HealthHandler),
            (r'/api/user/info', UserInfoHandler)
        ]
        conn = MongoClient("192.168.0.1", 27017)
        self.db = conn["test"]
        tornado.web.Application.__init__(self, handlers, debug=True)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
