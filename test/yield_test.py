def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)


g = foo()
print(next(g))
print("*" * 20)
print(next(g))

# 参考地址:
# https://blog.csdn.net/mieleizhi0522/article/details/82142856/
