import tornado.web
import json
import os
import time


class HealthHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps({"code": 200, "pid": os.getpid(), "start_time": time.time()}))
