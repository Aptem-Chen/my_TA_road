#! python3
# -*- coding: utf-8 -*-
import time
"""
初级写法2，仍然没有用到闭包和装饰器

将辅助功能（记录时间）抽离成一个辅助函数 count_time，在辅助函数count_time 中调用主要功能函数 print_odds
优点：解耦，函数职责分离
缺点：要通过辅助函数来调用主要功能函数，不方便
目标：能不能在调用主要函数时，自动完成对时间的统计？
"""


def count_time(func):
    """
    统计某个函数的运行时间
    """
    start_time = time.perf_counter()  # 起始时间
    func()  # 执行函数
    end_time = time.perf_counter()  # 结束时间
    print("It takes {} sec to find all the odds.".format(end_time - start_time))


def print_odds():
    """
    输出 0~100 之间所有奇数
    """
    for i in range(100):
        if i % 2 == 1:
            print(i)


if __name__ == '__main__':
    count_time(print_odds)
