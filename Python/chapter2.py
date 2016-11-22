# encoding utf-8
# print "%s is number %d" %("Python", 1)

# user = raw_input("enter your name:")

# print 'Your name is %s!' % (user)


# + - * / // ** and or not !=
# 字符串 索引操作符[] [:]切片操作符

pystr = "Python"

print pystr[2:5]

print pystr[:2]
print pystr[0:2]

print pystr[3:]
print pystr[-1]
print pystr * 2

# 列表list 元组tuple 可存储不同类型的对象

alist = [1,2,3,4]
print alist[:3]
print alist[0:3]

alist[0] = 10

atuple = ('robot',1,2,3)
print atuple[:3]
# tuple can not modify value

# dict
adict = {'host':'127.0.0.1'}
adict['port'] = 8888

adict.keys()
for key in adict:
    print adict[key]


if 1==1:
    print ''
elif 2==2:
    print ''
else:
    print ''


while(True):
    print 'hello'
    break

for item in [1,2,3]:
    print item, #多加个逗号 自动换行

sqdevents = [x**2 for x in range(8) if not x%2]

for i in sqdevents:
    print i


# 文件喝内建函数 open file

handle = open('file_name','r') # r读取 w写 a增加

for eachLine in handle:
    print eachLine

handle.close()

try:
    filename = raw_input('file name:')
    fobj = open(filename, 'r')
    for eachLine in fobj:
        print eachLine
    fobj.close()
except IOError, e:
    print 'file open error:', e

# function
def addMe2Me(x) :

    print 'apply + operation to argument'

    return x * 2

addMe2Me(5)


class Player(object):
    version = 0.1

    def __init__(self,name='xiaodong'):
        self.name = name

        print 'create class instance for ', name
    def showname(self):
        print 'my name is ', self.name
    def showver(self):
        print self.version
    def addMe2Me(self,x):
        return x * 2

player = Player()

player.showname()
player.showver()





