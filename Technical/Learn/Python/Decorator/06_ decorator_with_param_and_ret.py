#! python3
# -*- coding: utf-8 -*-
import time
"""
如果需要被装饰的函数，有形参，且有返回值
采用之前 04_decorator.py 中的写法，就会有一些问题
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


def count_odds(lim=100):
    """
    统计 0~lim 之间的所有奇数的个数
    """
    cnt = 0
    for i in range(lim):
        if i % 2 == 1:
            cnt += 1
    return cnt


# 对于有返回值的函数，闭包增强后，不能成功返回，但是成功增强了辅助功能
# 对于有参数的函数，闭包增强后，不能成功接收参数
if __name__ == '__main__':
    print("闭包前：")
    print(count_odds())  # 闭包前函数能正常返回，得到正确的值，但是自然没有被装饰的功能
    print("------------------")
    print("闭包后：")
    count_odds = count_time_wrapper(count_odds)
    print(count_odds())  # 闭包后的函数不能正常返回，得不到正确的返回值，
    print(count_odds(lim=200))  # 传入参数的话，会报错 TypeError: improved_func() got an unexpected keyword argument 'lim'
