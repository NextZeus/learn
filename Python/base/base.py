#openstack  开源云计算平台

#解释性语言

#源码不加密

#移动网站 卖服务 

# Sn=na1+n(n-1)d/2

# and or not

# \ 转译字符
# r '''...'''  批量转译字符 不需要 \
# -*- coding: utf-8 -*-   中文用UTF-8编码读取源代码

#print ''''''   //不能再用print u''''''

#list push insert(index,value) pop
# tuple 有序列表 创建后 不可修改
# tuple 单元素 (1,) 多元素可不加, ()可被理解为运算符

#tuple 中包括list  list值可改变
# t = ('a', 'b', ('A', 'B')) 不可变的tuple

#dict 字典 { a:1, b:2} 内部无序  str, number, tuple 都可以是key



d = {
	a:1
}
if 'a' in d
	print d['a']

print d.get('a')	

#遍历dict

for key in d
	print key

#set
#创建 set 的方式是调用 set() 并传入一个 list，list的元素将作为set的元素：

s = set(['A','B','C'])
length = len(s)

'A' in s #True

#遍历set 
for name in s
	print name

#更新set
s.add('D')
s.remove('D')

L = ['A','E']


for name in L:
	if name in s:
		s.remove(name)
	else :
		s.add(name)
print s


L = []
x = 1
while x <= 100:
    L.append(x * x)
    x = x + 1
print sum(L)


#函数
def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x


#函数返回多值  参数默认值

L = range(1,101)

print L[0:10]#从第1个数元素开始取，到第11元素结束

print L[2::3]#从第三元素开始取，每隔2个取一个元素

print L[4:50:5]#从第五个取，每隔4个取一个，‘开始元素’：‘最后元素’：‘取元素间隔’

L[-2:]

#字符串切片
'ABCD'[-2:] #'CD'
'abcd'.upper()

#定义函数
import math
def move(x,y,step,angle):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny

x,y = move(100,100,60, math.pi / 6)
print x,y


#enumerate(L) : [(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]
#zip(range(1,5), L)  :  enumerate(L)
L = ['Adam', 'Lisa', 'Bart', 'Paul']
r = range(1,5)
for index, name in zip(r,L):
    print index, '-', name


#迭代dict的value
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print d.values()
# [85, 95, 59]


#任务
#给定一个dict：

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

#请计算所有同学的平均分。
sum = 0.0
for v in d.itervalues():
    sum += v
    
print sum / len(d.values())

#1. values() 方法实际上把一个 dict 转换成了包含 value 的list
#2. 但是 itervalues() 方法不会转换，它会在迭代过程中依次从 dict 中取出 value，所以 itervalues() 方法比 values() 方法节省了生成 list 所需的内存

#迭代dict的key和value
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for k, v in d.iteritems():
    sum = sum + v
    print k, ':', v
print 'average', ':', sum / len(d)



