#! python3
# -*- coding: utf-8 -*-
import time

"""
最初级的写法，不涉及到python闭包和装饰器

函数逻辑（查找奇数）和辅助功能（记录时间）耦合在一起了。
缺点：不方便修改，容易引起bug
疑问：能不能将辅助功能从主要功能函数中抽离出来？
"""


def print_odds():
    """
    输出0~100之间所有奇数，并统计函数执行时间
    """
    start_time = time.perf_counter()  # 起始时间
    # 查找并输出所有奇数
    for i in range(100):
        if i % 2 == 1:
            print(i)
    end_time = time.perf_counter()  # 结束时间
    print("It takes {} sec to find all the odds.".format(end_time - start_time))


if __name__ == '__main__':
    print_odds()
