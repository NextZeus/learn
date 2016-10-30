def add(x,y,f):
    return f(x) + f(y)

add(-5,9,abs)

#map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回
def format_name(s):
    #return s.capitalize()
    #return s.title()
    return s[0].upper() + s[1:].lower()

print map(format_name, ['adam', 'LISA', 'barT'])

# reduce()函数也是Python内置的一个高阶函数。
#reduce()函数接收的参数和 map()类似，一个函数 f，一个list，
#但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值
def prod(x, y):
    return x*y

print reduce(prod, [2, 4, 5, 7, 12])

#reduce 接受第三个参数作为计算的初始值

#filter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list
#filter 过滤
import math

def is_sqr(x):
    r = int(math.sqrt(x))
    return r*r=x

print filter(is_sqr, range(1, 101))

#请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。
def calc_prod(lst):
def lazy_prod():
def f(x, y):
return x * y
    return reduce(f, lst, 1)
    return lazy_prod
f = calc_prod([1, 2, 3, 4])
print f()
