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
# 元组不可修改

# 字典
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
    print item, #自动换行

