#! python3
# -*- coding: utf-8 -*-
import time
"""
解决 06_..._ret.py 中提到的问题
这也是一个完整的 python 闭包（装饰器）写法
"""


def count_time_wrapper(func):
    """
    闭包，用于增强函数func，给函数func增加统计时间的功能
    """
    def improved_func(*args, **kwargs):  # 传可变参数，这样以应对各种情况的原函数，注：可变参数写法是固定的
        start_time = time.perf_counter()  # 起始时间
        ret = func(*args, **kwargs)  # 执行函数
        end_time = time.perf_counter()  # 结束时间
        print("It takes {} sec to find all odds.".format(end_time - start_time))
        return ret  # 返回原函数的返回值

    return improved_func


@count_time_wrapper
def count_odds(lim=100):
    """
    统计 0~lim 之间的所有奇数的个数
    """
    cnt = 0
    for i in range(lim):
        if i % 2 == 1:
            cnt += 1
    return cnt


if __name__ == '__main__':
    print("闭包前：")
    print(count_odds())  # 闭包前函数能正常返回，得到正确的值，但是自然没有被装饰的功能
    print("------------------")
    print("闭包后：")
    print(count_odds())
    print(count_odds(lim=200))  # 闭包后也可以正常传参、并的到返回值
