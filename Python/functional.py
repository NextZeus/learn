def add(x, y, f):
    return f(x) + f(y)


add(-5, 9, abs)


# map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回
def format_name(s):
    # return s.capitalize()
    # return s.title()
    return s[0].upper() + s[1:].lower()


print map(format_name, ['adam', 'LISA', 'barT'])


# reduce()函数也是Python内置的一个高阶函数。
# reduce()函数接收的参数和 map()类似，一个函数 f，一个list，
# 但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值
def prod(x, y):
    return x * y


print reduce(prod, [2, 4, 5, 7, 12])

# reduce 接受第三个参数作为计算的初始值

# filter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list
# filter 过滤
import math


def is_sqr(x):
    r = int(math.sqrt(x))
    return r * r


print filter(is_sqr, range(1, 101))


# 请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。
def calc_prod(lst):
    def lazy_prod():
        def f(x, y):
            return x * y
        return reduce(f, lst, 1)
    return lazy_prod
f = calc_prod([1, 2, 3, 4])
print f()


# 闭包

def count():
    fs = []
    for i in range(1, 4):
        def f(i):
            def g():
                return i * i

            return g

        r = f(1)
        fs.append(r)


f1, f2, f3 = count()
print f1(), f2(), f3()

# python中完善decorator

# @decorator可以动态实现函数功能的增加 但是经过@decorator改造后的函数，和原函数相比，除了多一点功能外，
# 其他地方也有不同
"""
在没有decorator的情况下，打印函数名
"""


def f1(x):
    pass


print f1.__name__
# f1

import time, functools


def performance(unit):
    def pref_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print 'call %s() in %f %s' % (f.__name__, t, unit)
            return r

        return wrapper

    return pref_decorator


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print factorial.__name__

# 偏函数
import functools

sorted_ignore_case = functools.partial(sorted, cmp=lambda s1, s2: cmp(s1.upper(), s2.upper()))
print sorted_ignore_case(['bob', 'about', 'zoo'])

# import 引入模块
try:
    import json
except ImportError:
    import simplejson as json
print json.dumps({'python': 2.7})

# __future__ 引入新版本功能
from __future__ import unicode_literals

s = 'am i an unicode'
print isinstance(s, unicode)


# 安装第三方模块
# pip[推荐] ; easy_install

class Person(object):
    pass


p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1, lambda p1, p2: cmp(p1.name, p2.name))

print L2[0].name
print L2[1].name
print L2[2].name


class Person(object):
    # 接受除了name,gender,birth外的任意参数
    def __init__(self, name, gender, birth, **kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        for k, v in kw.iteritems():
            setattr(self, k, v)

        xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

        print xiaoming.name
        print xiaoming.job
