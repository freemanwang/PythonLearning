#python中Number分为3种：整数、浮点数、复数

#py中所有整数都是int型，可以无限大，无限制
#如果数字过大，可使用下划线做分隔符
a = 1234_5678_9000
print(a)

#10进制不能以数字0开头
#二进制 0b开头
#八进制 0o开头
#十六进制 0x开头
#但打印都会十进制输出
n2 = 0b10
n8 = 0o10
n16 = 0x10
print(n2, n8, n16)      #2 8 16

#浮点数（小数）
#对浮点数进行运算时可能会得到一个不精确的结果
f1 = 0.1
f2 = 0.2
f = f1 + f2
print(f'0.1 + 0.2 = {f}')       #0.1 + 0.2 = 0.30000000000000004


##Number类的方法
#数学常量
#math.pi :圆周率
#maith.e :自然对数
import math
print(math.pi)  #3.141592653589793
print(math.e)   #2.718281828459045


#可以不添加 math. 前缀直接用的方法

#abs(x)   绝对值，直接用，对所有Number都可用
#还有个math.fabs(),需要导入模块后使用，仅对int和float可用
print(abs(-10), abs(-5.5))  #10 5.5

#max() 方法返回给定参数的最大值，参数可以为序列。

#min() 方法返回给定参数的最小值，参数可以为序列。

#混入其他类型就报错，比如有个字符'a'
print(max(1, 2, 3, 4, 5))   #5
list = [1, 2, 3, 4, 5, 7.8]
print(max(list))    #7.8
print(min(list))    #1
tuple = (1, 2, 3, 4, 5, -3)
print(max(tuple))    #5
print(min(tuple))    #-3
set = {1, 2, 3}
print(max(set))    #3

#math.pow(x, y [,z]) 方法返回 xy（x的y次方） 的值。
#函数是计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z
x = 3
y = 4
z = 5
print(f'{x}^{y}=',pow(x,y), '返回类型是', type(pow(x,y)))     #3^4= 81 返回类型是 <class 'int'>
print(f'{x}^{y}%{z}=',pow(x,y,z))   #1
print(f'{float(x)}^{float(y)}%{z}=',pow(x,y,z), '返回类型是', type(pow(x,y)))
#3.0^4.0%5= 1 返回类型是 <class 'int'>

#round() 方法返回浮点数x的四舍五入值。
#round( x [, n]  )
#x -- 数字表达式。
#n --小数点后留多少位，默认为0
x = 123.4567
print(f'round({x})=',round(x), type(round(x)))  #round(123.4567)= 123 <class 'int'>
print(f'round({x}, 2)=',round(x, 2), type(round(x,2))) #round(123.4567, 2)= 123.46 <class 'float'>
print(f'round({x}, 4)=',round(x, 4))



#必须添加 math. 前缀才能用的方法

#math.ceil( x )  向上取整.不可直接使用，需要导入math模块
#math.floor(x)  向下取整.不可直接使用，需要导入math模块
import math
a = 1.5
print(f'a={a}, math.ceil(a)={math.ceil(a)}')    #a=1.5, math.ceil(a)=2
print(f'a={a}, math.floor(a)={math.floor(a)}')  #a=1.5, math.floor(a)=1

#sqrt() 方法返回数字x的平方根。返回值为float型
x = 9
print(f'sqrt({x})=', math.sqrt(x), type(math.sqrt(x)))  #sqrt(9)= 3.0 <class 'float'>

#math.exp() 方法返回x的指数,e^x
#math.exp()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。
print(f'e^3={math.exp(3)}') #e^3=20.085536923187668

#math.modf( x )  返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
#返回的类型是tuple,小数部分在前，整数部分以浮点数形式在后
a = 10
b = 56.789
print(f'math.modf({a})=',math.modf(a), '返回类型是',type(math.modf(a)))
#math.modf(10)= (0.0, 10.0) 返回类型是 <class 'tuple'>
print(f'math.modf({b})=',math.modf(b))  #math.modf(56.789)= (0.7890000000000015, 56.0)

#数值比较,意义不大
#(x>y)-(x<y):如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
a = 1
b = 2
print((a>b)-(a<b))  #-1

#math.log(x [,底]) 返回对数，默认是e做底，可设定底.
#返回的结果都是浮点数，哪怕结果是整数，也会用浮点数返回
#math.log()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。
print(f'ln(PI)={math.log(math.pi)}')    #ln(PI)=1.1447298858494002
print(f'log2(4)={math.log(4, 2)}')    #log2(4)=2.0
print(type(math.log(1)))    #<class 'float'>

#math.log10() 方法返回以10为基数的x对数，x>0。
#有math.log()可设定底数，这个意义不大
#math.log10()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。


##随机数方法
#需要 import random  后方可使用
#全都不可直接使用，需要 random. 前缀
import random

#random.choice() 方法返回一个列表，元组或字符串的随机项。
list = [1, 2, 3, 'a', 'b', 'c']
str = 'hello world'
print(random.choice(list))  #多次运行结果不一
print(random.choice(str))  #多次运行结果不一

#random.randrange() 方法返回指定递增基数集合中的一个随机数，基数缺省值为1。
#random.randrange ([start,] stop [,step])
#start -- 指定范围内的开始值，包含在范围内。默认为0
#stop -- 指定范围内的结束值，不包含在范围内。
#step -- 指定递增基数。默认为1
print('random.randrange(100):', random.randrange(100))  #[0,100) 随机整数
print('random.randrange(10,100):', random.randrange(100))  #[10,100)随机整数
print('random.randrange(1,100, 2):', random.randrange(100))  #1-99 随机奇数

#random.random() 方法返回随机生成的一个实数，它在[0,1)范围内
#random.random()
print('random.random():',random.random())   #[0,1)之前小数，位数挺多的

#random.seed([x]) 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。
#x -- 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
random.seed()
print ("使用默认种子生成随机数：", random.random())  #每次种子都会变

#random.shuffle() 方法将序列的所有元素随机排序。
#random.shuffle (list ) 不返回什么，直接对list本身进行操作。
#注意list是可更改类型
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('list:',list)
random.shuffle(list)
print('shuffle(list)', list)



