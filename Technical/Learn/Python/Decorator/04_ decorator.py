#! python3
# -*- coding: utf-8 -*-
import time
"""
什么是语法糖（Syntactic sugar）？
·指计算机语言中添加的某种语法，这种语法对语言的功能没有影响，但是更方便程序员使用。
    ·语法糖没有增加新功能，只是一种更方便的写法。
    ·语法糖可以完全等价的转换为原本非语法糖的代码。

最终写法，利用到了装饰器
通过装饰器进行函数增强，只是一种语法糖，本质上跟 03_function_closure_inclosure.py 的程序完全一样

通过 01_..._infunc.py ~ 04_decorator.py 
可以总结出，装饰器的使用方法就是： @闭包函数名
装饰器其实就是闭包写法的语法糖，功能上完全等价于闭包函数的使用

注：
·装饰器在第一次调用被装饰函数时进行增强
    ·增强时机 -> 在第一次调用之前
    ·增强此时 -> 只增强一次
"""


def count_time_wrapper(func):
    """
    闭包，用于增强函数func，给函数func增加统计时间的功能
    """
    def improved_func():
        start_time = time.perf_counter()  # 起始时间
        func()  # 执行函数
        end_time = time.perf_counter()  # 结束时间
        print("It takes {} sec to find all odds.".format(end_time - start_time))

    return improved_func


@count_time_wrapper
def print_odds():
    """
    打印 0~100 之间所有的奇数
    """
    for i in range(100):
        if i % 2 == 1:
            print(i)


if __name__ == '__main__':
    # 装饰器等价于在第一次调用函数时执行以下语句：
    # print_odds = count_time_wrapper(print_odds)
    print_odds()
