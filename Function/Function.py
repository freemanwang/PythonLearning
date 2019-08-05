#function 函数
#函数也是对象（对象是内存中专门用来存数据的一块区域）
#可以把函数理解成“保存可执行代码的对象，并且可以在需要时多次调用”

#创建函数
#def 函数名([形参1，形参2....]):
#    代码块

def printHello():
    print('Hello WorLd！原初限定版！')
#调用
printHello()
#函数也是对象，和别的对象在本质上没区别，都是存数据的嘛
#函数名可以理解成变量，根据函数名记录的地址可以找到内存里的函数对象
print(printHello)   #<function printHello at 0x000001966741C2F0>

#参数传递方式
#函数在调用时，编译器不会检查实参的类型。
#实参可以传递任意类型的对象
#函数也可以作为传递的参数，称为 回调函数

#将外部变量传给函数，并在函数中对其进行修改，外部变量会不会改变呢?
#如果形参指向的是一个对象，那么通过形参修改对象时，实参会跟着改变
#如果形参指向的是一个变量，那么对形参进行修改不影响变量
def argChange(a):
    if isinstance(a, int):
        a = 20
    elif isinstance(a, list):
        a[0] = 20
    else:
        pass
    print(f'print by function.\targ = {a},id({a})={id(a)}')
b = 10
c = [1,2,3]
#参数是不可变类型时，实参和形参的地址不一样
argChange(b)    #print by function.	arg = 20,id(20)=140709193901488
print(f'arg={b},id(arg)={id(b)}')   #arg=10,id(arg)=140709193901168
#参数是可变类型时，实参和形参地址一样
argChange(c)    #print by function.	arg = [20, 2, 3],id([20, 2, 3])=1869309436552
print(f'arg={c},id(arg)={id(c)}')   #arg=[20, 2, 3],id(arg)=1869309436552

#直白的说，传的参是可变更类型的话，函数进行的修改会同步到参数本身
#传的参是不可变更类型的话，函数的修改不影响参数本身
#如果传递的是一个可变对象，为了确保不被改变，可以copy过去或者传切片


#参数分4种

# 1.必需参数，最简单最常用的方法
#必须按定义顺序传入，数目必须匹配。
def originArg(a,b):
    #a,b同为Number，函数功能是求和
    return a+b
print('1 + 2 =',originArg(1,2))     #1 + 2 = 3

# 2.关键字参数
#使用关键字确认传入的参数值，允许顺序不一致。
def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return
printinfo(age=50, name="runoob")
#名字: runoob
#年龄: 50

# 3.默认参数
#调用函数时，如果没有传递参数，则会使用默认参数。
#在定义函数时，就_给参数赋默认值即可
def printinfo(name, age=18):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return
printinfo('Alice')
#名字:  Alice
#年龄:  18

# 4.可变参数
#可能需要函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，声明时不会命名
#不定参用 '*'时，只能接受位置参数，传入的参会当成元组Tuple。
#如同解包时的做法， * arg 不一定要在最后，其实在哪都行，但只能有1个
#传参时，位置参数在最前，关键字参数一定在位置参数之后，否则报错
def printinfo(arg1, *var_tuple):
    #"打印任何传入的参数" 
    print(arg1)
    print(var_tuple,type(var_tuple))
printinfo(70, 80, 90, 100)
#70
#(80, 90, 100) <class 'tuple'>

#如果在形参开头用 * ，则要求所有参数必须用关键字参数传递,否则怎么确定截止
def printinfo(* var, a, b, c):
    #"打印任何传入的参数"  
    print(f'a={a},b={b},c={c}')
    print(f'不定参为：{var},类型是{type(var)}')
printinfo(0, 1, 2, 3, 4,a='a',b='b', c='c')
#a=a,b=b,c=c
#不定参为：(0, 1, 2, 3, 4),类型是<class 'tuple'>

# ** 形参差不多，区别在于接受的数据会保存到dict字典中
# ** 形参只能有1个，且必须写在所有参数的最后
def printinfo(a, b, c, **var_dict):
    print(f'a={a},b={b},c={c}')
    print(f'不定参为：{var_dict},类型是{type(var_dict)}')
printinfo( k1=1, k2=2, k3=3, a='a',b='b', c='c',)
#a=a,b=b,c=c
#不定参为：{'k1': 1, 'k2': 2, 'k3': 3},类型是<class 'dict'>
#PS:既然传递的是字典，那就要有键值对。之前一直报错，就是没给对参数

#参数的解包

#用序列来传递参数时，可以在序列前添加 * ，这样自动将序列里元素逐一对应给形参
#意思是，list，tuple甚至str都可以做实参。当然，长度一定要和型参数一致
def printinfo(a, b, c, d):
    print(f'a={a},b={b},c={c},d={d}')
t = (1,2,3,4)
st = 'abcd'
printinfo(*t)   #a=1,b=2,c=3,d=4
printinfo(*st[:])  #a=a,b=b,c=c,d=d

#用dict传参时， ** 对其解包
#顺带一说，key的名字必须和形参名一致，否则无法接收参数。
#d = dict(k1=1, k2=2, k3=3, k4=4)  一开始这个dict传过去就报错
d = {'a':1, 'b':2, 'c':3, 'd':4}
printinfo(**d)  #a=1,b=2,c=3,d=4
#a=1,b=2,c=3,d=4


#匿名函数
#python使用 lambda 来创建匿名函数。所谓匿名，意即不再使用 def 语句这样标准的形式
# 定义一个函数。* lambda 只是一个表达式，函数体比 def 简单很多。
#*lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# * lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
#*虽然lambda函数看起来只能写一行，却不等同于C或C + +的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
# 语法
#lambda 函数的语法只包含一个语句，如下：
#* lambda [arg1[, arg2, .....argn]]:expression

sum = lambda arg1, arg2: arg1 + arg2
print("相加后的值为 : ", sum(10, 20))
#相加后的值为: 30

##返回值
#返回值除了可以是数据，还可以是函数，只要你想return它，当然，注意作用域。
#不写return或者return后不接东西，那函数调用后就返回None


