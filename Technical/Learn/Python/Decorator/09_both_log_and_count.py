#! python3
# -*- coding: utf-8 -*-
import time


def count_time_wrapper(func):
    """
    闭包：统计函数运行时间
    """
    def improved_func(*args, **kwargs):
        start_time = time.perf_counter()
        ret = func(*args, **kwargs)
        end_time = time.perf_counter()
        print("It takes {} sec to find all odds.".format(end_time - start_time))
        return ret

    return improved_func


def log_wrapper(func):
    """
    闭包：日志功能
    """
    def improved_func(*args, **kwargs):
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        ret = func(*args, **kwargs)
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        print("Logging: func:\"{}\" runs from {} to {}".format(func.__name__, start_time, end_time))
        return ret

    return improved_func


@count_time_wrapper
@log_wrapper
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
    print(count_odds(200))
