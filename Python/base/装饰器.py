#!/usr/bin/env python
# encoding: utf-8

def new_fn(f):
    def fn(x):
        print 'call '+ f.__name__+'()'
        return f(x)

    return fn

#高阶函数 返回一个新函数
@new_fn
def f1(x):
    return x*2

f1(5)
