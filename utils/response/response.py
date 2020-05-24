class HttpCode(object):
    SUCCESS = 200
    FORBIDDEN = 403
    NOT_FOUND = 404
    SERVER_INTERNAL_ERROR = 500
    REQUEST_PARAM_ERROR = 1001


class ErrMsg(object):
    SUCCESS = "success"
    FORBIDDEN = "请求被禁止"
    NOT_FOUND = "请求的资源找不到"
    SERVER_INTERNAL_ERROR = "服务器错误"
    REQUEST_PARAM_ERROR = "请求参数错误"


class APiResult(object):
    def __init__(self, code, msg, response):
        self.code = code
        self.msg = msg
        self.data = response
