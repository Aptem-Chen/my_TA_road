#! python3
# -*- coding: utf-8 -*-
"""
多个装饰器情况下的分析：
首先将装饰器等价转换为闭包写法，这样便于分析
分析结论看下文
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


def original_func():
    print("call original_func")


if __name__ == '__main__':
    """
    分析：
    闭包写法可以看出，装饰器装饰的顺序，其实就是闭包的顺序
    且每一次闭包，相当于将上一次闭包后的函数进行再一次闭包
    比如这个例子中：
        原函数首先被装饰器闭包，得到"装饰函数1"
        然后装饰器2，闭包过程其实装饰的不再是原函数，而且"装饰函数1"
        
        所以会发现，输出结果的顺序是：
            set func1
            set func2
        
        当全部闭包（装饰）之后，执行原函数（其实是已经多次闭包后的函数），
        就像从剥洋葱一样，一层一层执行，所以输出结果是：
            call func2
            call func1
    做个比喻的话，多次闭包（装饰），就是给函数包上一层层包装纸，一层套一层，
    执行的时候，就相当于将这个有好几层包装纸的函数，一层层拆开。
    
    所以装饰器装饰顺序（打包装）是正序的
    增强功能的执行顺序（拆包装）是逆序的
    """
    # 闭包
    # original_func = wrapper1(wrapper2(original_func))
    # 分解写法
    original_func = wrapper1(original_func)  # 装饰器1
    original_func = wrapper2(original_func)  # 装饰器2
    print("----------")
    original_func()
