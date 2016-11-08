#!/usr/bin/env python
# encoding: utf-8

#自适应参数个数
def log(f):
    def fn(*args, **kw):
        print 'call'+f.__name__+'()...'
        return f(*args,**kw)
    return fn

#编写一个@performance 打印函数调用的时间

import time

def performance(unit):
    def pref_decorator(f):
        def fn(*args,**kw):
            t1 = time.time()
            r = f(*args,**kw)
            t2 = time.time()
            t = (t2 - t1 )*1000 if unit == 'ms' else (t2 - t1)
            print 'call %s() in %f %s' %(f.__name__, t, unit)
            return r
        return fn
    return pref_decorator

@performance('ms')#等同与 pref_decorator = performance('ms)   factorial = pref_decorator(factorial)
def factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
print factorial(10)
