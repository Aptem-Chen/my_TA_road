#! python3
# -*- coding: utf-8 -*-
"""
一个完整的 python 闭包（装饰器）写法
"""


def general_wrapper(func):
    def improved_func(*args, **kwargs):  # 接收原函数参数
        ret = func(*args, **kwargs)  # 传入参数并记录返回值
        return ret  # 返回原函数返回值

    return improved_func  # 返回闭包增强后函数
