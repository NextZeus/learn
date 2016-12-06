#!/usr/bin/env python
# encoding: utf-8

#lambda 关键词表示匿名函数 冒号前面的x 表示函数参数

map(lambda x: x*x, [1,2,3,4,5])

#等同
def f(x):
    return x * x

def is_not_empty(s):
    return s and len(s.strip()) > 0

print filter(lambda s:s and len(s.strip()) > 0), ['test','',None,'   ','END']
