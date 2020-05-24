def fbnq(n):
    if n < 1:
        print('输入有误！')
        return -1
    if n == 1 or n == 2:
        return 1

    return fbnq(n - 2) + fbnq(n - 1)
