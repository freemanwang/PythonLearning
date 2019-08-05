#函数在python中是一等对象
#一等对象的特点：
#   -对象在运行时创建的（py中所有对象都这样
#   -能赋值给变量或作为数据结构中的元素（可以存进list或dict）
#   -能作为参数传递
#   -能作为返回值返回
#   其实，py中所有对象都是一等对象。之所以要强调，因为有些语言中函数不是一等对象。

#高阶函数
#高阶函数至少要符合以下两个特点中的一个
#   -1.接收一个或多个函数做参数
#   -2.将函数作为返回值返回
#当我们使用一个函数做参数时，实际上是把代码传给了函数

#假如我需要不同情况时用多个功能：
#   1.筛选出list中的偶数/偶数
#   2.筛选出list中的3的倍数
#   3.筛选出list中大于5的数

def select(func, lst):
    new_list = []
    for i in lst:
        if func(i):
            new_list.append(i)
    return new_list

def getmean(i):
    if i % 2 == 0:
        return True
    return False

def getodd(i):
    if i % 2 != 0:
        return True
    return False

def get3Times(i):
    if i % 3 == 0:
        return True
    return False

lst = [1,2,3,4,5,6,7,8,9,10]
print(f'lst中偶数有：{select(getmean,lst)}') #lst中偶数有：[2, 4, 6, 8, 10]
print(f'lst中奇数有：{select(getodd,lst)}')  #lst中奇数有：[1, 3, 5, 7, 9]
print(f'lst中3的倍数有：{select(get3Times,lst)}') #lst中3的倍数有：[3, 6, 9]
#根据传入的函数的不同实现功能的不同。PS：传函数用的是函数名，不带()的





#内建函数filter()
#可以从序列中过滤出符合条件的元素，保存到一个新序列中
#参数：
#   -1.函数，根据该函数来过滤序列（可迭代的结构）
#   -2.需要过滤的序列（可迭代的结构）
#返回值：
#   -过滤后的新序列（可迭代的结构）

obj = filter(getmean,lst)
print(obj)  #<filter object at 0x0000027EBF42A1D0>
for t in obj:
    print(t,end='  ')   #2  4  6  8  10
print()

#为了作为参数，在全局变量定义了一个函数，一般不这么做，代价略大。
#所以匿名函数就用在这里了
#用匿名函数，用完一次就从内存清除，高效简洁
#问题是，匿名函数只能实现较简单的功能，无法完成复杂工作

#语法： lambda 参数列表 : 返回值
add = (lambda a,b : a+b)
print(add(20,30))   #50

#用匿名函数做参数使用fileter()
#功能：找出lst中4的倍数
T4 = filter((lambda i: i%4==0), lst)
print(T4)   #<filter object at 0x0000016B944BA2B0>
print(list(T4)) #[4, 8]






#内建函数map()
# 可以对可迭代对象中所有元素做指定的操作，然后将其添加到一个新对象中返回

#比如，把列表中所有立方
l = [1,2,3,4]
r = map(lambda i : i**3, l)
print(list(r))  #[1, 8, 27, 64]





#内建函数sort()  | [使用方法 list.sort()]
#功能是对list列表中元素进行排序。不返回，作用于调用者自身
#sort()方法默认是直接比较列表中元素的大小，然后递增排序
#在python中，str直接可以直接用 '>' | '<'进行比较；但是，Number和str不能直接比
l = ['kkkkkkkk','aa', 'ffff','c']
l.sort()
print(l)    #['aa', 'c', 'ffff', 'kkkkkkkk']

#在sort()中可以接受一个关键字参数  key，这个key是函数名
#每次都会以列表中一个元素作为参数来调用函数，并且使用函数的返回值来比较大小
l = ['kkkkkkkk','aa', 'ffff','c']
l.sort(key=len) #传入的参数key是len，按照长度进行排序
print(l)    #['c', 'aa', 'ffff', 'kkkkkkkk']

l2 = [34, 12, 555, 58, '13', '25', 2]
l2.sort(key=int)  #字符串和int没法直接比大小，那就把参数int一下，转成int再比
print(l2)   #[2, 12, '13', '25', 34, 58, 555]
#PS:类型转换后拿去比较了，并不是要修改类型，所以字符串型的元素在列表中类型没变
#PPS：key后是个作用于元素的函数，别把它当成类型选择，就像我一开始在list里写了'abc'
#     这样的元素，然后报错了。key=int并不是筛选出int来比，而是把元素用int()转型






#内建函数sorted()
#这个函数类似sort，但是有2个关键区别：
#   -1.sorted()可以对任意的序列进行排序
#   -2.sorted()不影响原本的对象，而是返回排序后的新对象
L3 =[34, 12, 555, 58, '13', '25', 2]
print("排序前L3：",L3)   #排序前L3： [34, 12, 555, 58, '13', '25', 2]
l3 = sorted(L3,key=int)  #排序并不作用域L3，而是返回一个排好序的新序列
print('排序后L3:',L3)    #排序后L3: [34, 12, 555, 58, '13', '25', 2]
print('递增序列：',l3)   #递增序列： [2, 12, '13', '25', 34, 58, 555]

#顺带一说，这里就是sorted()比sort()应用范围广的例子
strL = 'hello world again!'
#print(strL.sort())  #报错。AttributeError: 'str' object has no attribute 'sort'
strLS = sorted(strL)
print(strLS)    #[' ', ' ', '!', 'a', 'a', 'd', 'e', 'g', 'h', 'i', 'l', 'l', 'l', 'n', 'o', 'o', 'r', 'w']





#闭包:对外部封闭
#将函数作为返回值返回，也是一种高阶函数
#意义在于，可以利用访问域控制一些变量的访问
#通过闭包可以创建一些只有当前函数才能访问的变量
#可以将一些私有数据藏到闭包中

# def fn():
#     private = []
#     def getPrivate(st=None):
#         if st:
#             pri.append(st)
#         return private
#     return getPrivate()
#
# pri = fn()
# print(pri('dairy'))  #20
#变量不会被更改。






