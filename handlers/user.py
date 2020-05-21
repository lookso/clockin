import tornado.web
from pymongo import MongoClient


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("this index html")


class RegisterHandler(tornado.web.RequestHandler):
    def post(self):
        name = self.get_argument('name')
        if not name:
            self.finsh("this register")


class LoginHandler(tornado.web.RequestHandler):

    def post(self):
        name = self.get_argument("name")
        pwd = self.get_argument("pwd")
        # 判断变量是否为None
        if name is None:
            self.finish("params name err")
        if not pwd:
            self.finish("params pwd err")
        self.finsh("ok")


class UserInfoHandler(tornado.web.RequestHandler):

    def get(self):
        name = self.get_argument("name")
        pwd = self.get_argument("pwd")
        if name is None:
            self.finish("params name err")
        if not pwd:
            self.finish("params pwd err")
        self.set_status(200)
        human = {"name": "jack", "age": 11, "sex": 1}
        for k, v in human.items():
            print(k, v)

        coll = self.application.db.names
        book = coll.find_one({"nums": 1})
        name = None
        if book:
            name = book['name']
        self.finish(name)
        return
