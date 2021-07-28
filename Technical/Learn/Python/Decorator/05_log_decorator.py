#! python3
# -*- coding: utf-8 -*-
import time


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
