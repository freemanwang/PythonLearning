#List是python一个对象
#可保存有序数据
## 列表（List）
#list写在方括号[]间，元素用逗号','隔开。元素类型不限。
#list中元素是可变的。
#列表其实就是数组，这么就好理解了
#列表是存储对象的对象，列表内可(同时)存任意类型的对象

t = ['a', 'b', 'c', 1, 2]
# 用下标来访问列表内的元素
print(t[2])   #c

#切片：做切片时，返回一个新的列表，不影响原列表。list[:]返回一个完全相同的列表
print(t[1:3])   #['b', 'c'],这里要注意前面是下标，后面是第i个元素；这里是从第2个开始，到第3个结束
#t[a,b]    理解成t[a] --> t[b-1]；或者说，下标是[a,b)
print(t[2 :])  #['c', 1, 2],下标2至结束
print(t[1 : 4 : 2])  #['b', 1] , 下标1开始，第4个元素结束，步长为2

print(t[-3])   #c   下标-3表示倒数第3个
print(t[-5:-3]) #['a', 'b']  从下标-5开始，至下标-3-1即-4.和正数下标时逻辑一致


# + 和 * 操作
alist = [1,2,3] + [4, 5, 6]
print(alist)   #[1, 2, 3, 4, 5, 6]   拼接，就像字符串相应操作一样
print(alist * 2)     #[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

#函数

# in 和 not in    检查指定元素是否存在于列表中
Bob = 'Bob'
Eve = 'Eve'
people = ['Alice', 'Bob', 'Carol', 'David']
print(Bob in people)    #True
print( Eve not in people)   #True

#min(list) max(list) 获取List中最小/最大值
alist = [1, 2, 3, 4, 5]
print(f'max = {max(alist)},min = {min(alist)}')   #max = 5,min = 1

#list(obj) 方法  将obj转成list,obj可以是str或tuple，不可以是Number
atuple = (1, 2, 'abc')
tlist = list(atuple)
slist = list('abc')
#nlist = list(123.32)
print(type(tuple),type(tlist))  #<class 'type'> <class 'list'>
print(type(slist),slist)  #<class 'list'> ['a', 'b', 'c']

#通过切片删除部分元素
lst = [1, 2, 3, 4, 5]
del lst[2:4]
print(lst)  #[1, 2, 5]   删除成功
#通过切片赋值时，只能使用序列
lst[1:2] = '你好世界'
print(lst)  #[1, '你', '好', '世', '界', 5]
lst[1:1] = ['插入新元素']
print(lst)  #[1, '插入新元素', '你', '好', '世', '界', 5]


#del  删除某元素
lst = ['你好', '我好', '大家好']
del lst[1]
print(lst)  #['你好', '大家好']

#str(list) 将list转换成str格式，注意， [] , 等是在str内部的
print(str(lst),type(str(lst)))  #['你好', '大家好'] <class 'str'>
str1 = str(lst)
i = 0
while i < len(str1):
    print(str1[i] ,end='|')     #[|'|你|好|'|,| |'|大|家|好|'|]|1
    i+=1



#方法
#list.index(obj)  返回obj在list中的下标。不存在则报ValueError异常
try:
    print(people.index('Bob'))
    print(people.index('Eve'))
except ValueError:
    print()

#list.append(obj)  在末尾添加新对象
al = [1, 2]
al.append(123)
print(al)   #[1, 2, 123]

#list.extend(seq)  用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
#seq -可以是列表、元组、集合、字典，若为字典,则仅会将键(key)作为元素依次添加至原列表的末尾。
L1 = [1, 2, 3]
L2 = ['a', 'b', 'c']
L1.append(L2)
print(L1)  #[1, 2, 3, ['a', 'b', 'c']]
L1 = [1, 2, 3]
L1.extend(L2)
print(L1)   #[1, 2, 3, 'a', 'b', 'c']
#注意append()和extend()的区别

#Num:list.count(obj) 统计某个元素在列表中出现的次数,返回出现的次数（整数）
print(al.count(1))  #1
print(al.count(3))  #0

#list.insert(index, obj)  显然，把obi插入下标所在
L = ['abc', '123', 456]
L.insert(2, 'def')
print(L)    #['abc', '123', 'def', 456]

#Obg:list.pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
print(L.pop())  #456
print(L.pop(2)) #def

#list.remove() 函数用于移除列表中某个值的第一个匹配项。
#注意，仅作用于第一个匹配项
#无返回值，对list进行操作
#若无欲删除对象，报ValueError 异常
L = ['a', 'b', 'c', 'a', 1, 2, 3]
try:
    L.remove('a')
    L.remove(20)
except ValueError as err:
    print(err)  #list.remove(x): x not in list
print(L)    #['b', 'c', 'a', 1, 2, 3]

#list.reverse()  反向列表元素
L = [1,2,3,4,5]
L.reverse()
print(L)    #[5, 4, 3, 2, 1]

#list.clear() 清空列表
L.clear()
print(L)    #[]

#list.sort( key=None, reverse=False)
#key -- 主要是用来进行比较的元素,感觉可能元素是大对象时才用得上
#reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
aList.sort()
print("List : ", aList) #List :  ['Facebook', 'Google', 'Runoob', 'Taobao']
aList.sort(reverse=True)
print("List : ", aList) #List :  ['Taobao', 'Runoob', 'Google', 'Facebook']

#list.copy() 用于复制列表，返回新生成的列表，类似于 a[:]。
L1 = [1,2,3]
L2 = L1.copy()
print('id(L1):',id(L1))     #id(L1): 2502425762760
print('id(L2):',id(L2))     #id(L2): 2502425678920
#L1和L2地址不一样即可。实际上每次运行分配给L1和L2的地址都在变

#遍历列表（序列/Sequence）
stu = ['张三', '李四', '王五', '赵六']
i=0
while i < len(stu):
    print(stu[i])
    i+=1

#每次执行时，将list中元素赋值给obj
for obj in stu:
    print(obj)  #遍历输出

for i in range(2,3):
    print(i)        #2
    print(stu[i])       #进打印了stu[2]，range(a,b) 是[a,b)

for i in range(4):
    print(i )   #0-3
    print(stu[i])   #全员





