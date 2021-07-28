#! python3
# -*- coding: utf-8 -*-
"""
经典装饰器思考题：
当有多个装饰器的时候，装饰函数的顺序是怎样的？
调用原函数时，各个装饰器的增强功能执行顺序又是怎样的？
"""

def wrapper1(func1):
    print("set func1")  # 在 wrapper1 装饰函数时输出

    def improved_func1():
        print("call func1")  # 在 wrapper1 装饰过的函数被调用时输出
        func1()

    return improved_func1


def wrapper2(func2):
    print("set func2")  # 在 wrapper2 装饰函数时输出

    def improved_func2():
        print("call func2")  # 在 wrapper2 装饰过的函数被调用时输出
        func2()

    return improved_func2


@wrapper1
@wrapper2
def original_func():
    pass


if __name__ == '__main__':
    original_func()
    print("----------")
    original_func()
