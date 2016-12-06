#!/usr/bin/env python
# encoding: utf-8

#在函数内部定义的函数和外部定义的函数是一样的，只是他们无法被外部访问

#希望一次返回3个函数，分别计算1*1,2*2,3*3

def count():
    fs = [];
    for i in range(1,4):
        def f(i):
            def g():
                return i * i
            return g

        r = f(i)
        fs.append(r)
    return fs

f1 ,f2, f3 = count()
print f1(),f2(),f3()
