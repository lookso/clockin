import tornado.web
import json
from utils.response.response import *
from utils.utils.utils import *
from utils.utils.decorator import *
from collections.abc import Iterable
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

    def get(self):
        pass

    def post(self):
        name = self.get_argument("name")
        pwd = self.get_argument("pwd")
        # 判断变量是否为None
        if name is None:
            self.finish("params name err")
        if not pwd:
            self.finish("params pwd err")

        self.finish(json.dumps(
            APiResult(HttpCode.SUCCESS, ErrMsg.SUCCESS, {}).__dict__))


def maxNum(a, b):
    if a > b:
        return a
    else:
        return b


class UserInfoHandler(tornado.web.RequestHandler):

    def post(self, *args, **kwargs):
        pass

    def get(self):

        name = self.get_argument("name")
        pwd = self.get_argument("pwd")

        if name is None:
            self.finish(json.dumps(
                APiResult(HttpCode.REQUEST_PARAM_ERROR, ErrMsg.REQUEST_PARAM_ERROR, {}).__dict__))

        if not pwd:
            self.finish(json.dumps(
                APiResult(HttpCode.REQUEST_PARAM_ERROR, ErrMsg.REQUEST_PARAM_ERROR, {}).__dict__))

        self.set_status(200)
        human = {"name": "jack", "age": 11, "sex": 1}
        for k, v in human.items():
            print(k, v)
        coll = self.application.db.names
        book = coll.find_one({"nums": 1})
        bd = {}
        if 'name' in book:
            bd['name'] = book['name']

        if 'nums' in book:
            bd['nums'] = book['nums']

        if bd.get('name') and bd.get('nums'):
            bd["max"] = maxNum(10, 20)
            bd['fbnq'] = fbnq(maxNum(1, 5))
            bd['decorator'] = now()

        '''是否可迭代'''
        bd['iterable'] = isinstance(bd, Iterable)
        self.finish(json.dumps(
            APiResult(HttpCode.SUCCESS, ErrMsg.SUCCESS, bd).__dict__))
        return
