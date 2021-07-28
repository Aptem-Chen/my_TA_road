#! python3
# -*- coding: utf-8 -*-
import time
"""
什么是闭包函数？
·函数式语言（函数时一等公民，可作为变量使用）中的术语。
·函数闭包定义：首先它本身是一个函数，然后，它的形式参数和返回值也都是函数对象，返回值的函数是在该闭包函数内定义的
    ·用户增强函数功能
    ·面向切面编程（AOP）

通过闭包增强主要功能函数 print_odds，给它增加一个统计时间的功能
缺点：需要显示进行闭包增强
"""


def print_odds():
    """
    输出 0~100 之间所有奇数
    """
    for i in range(100):
        if i % 2 == 1:
            print(i)


# 闭包本质上是一个函数
# 闭包函数的形参和返回值也都是函数对象
# 闭包函数的返回值函数对象，是对传入的函数对象进行增强的结果
def count_time_wrapper(func):
    """
    闭包，用于增强函数func：给函数func增加统计时间的功能
    """
    def improved_func():
        start_time = time.perf_counter()  # 起始时间
        func()  # 执行函数
        end_time = time.perf_counter()  # 结束时间
        print("It takes {} sec to find all the odds.".format(end_time - start_time))

    return improved_func


if __name__ == '__main__':
    # 调用count_time_wrapper增强函数
    print_odds = count_time_wrapper(print_odds)
    print_odds()
