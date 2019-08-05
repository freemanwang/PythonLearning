#python中有2种作用域
#   1.全局作用域
#       全局作用域程序执行时创建，程序结束后销毁
#       所有函数以外的区域就是全局作用域，在全局作用域定义的变量就是全局变量
#       全局变量在函数任意位置被访问

#   2.函数作用域
#       函数调用域在函数调用时创建，函数结束时销毁
#       函数每次调用都产生一个新的函数作用域
#       函数作用域定义的变量，是局部变量，只能在函数内部被访问

#和其他程序设计语言一样

#变量查找
#   优先在当前作用域查找，有则使用
#   如果没查到，去上一级作用域查找，有则使用，不行就更上级，以此类推
#   如果全局作用域都没找到，那就抛出异常NameError

#如果希望在函数内部修改全局变量，需要global关键字来声明变量，且变量名和该全局变量一样
a = 20
def modA():
    global a
    a = 30
    print(f'函数内部a={a}')     #函数内部a=30

modA()
print(f'函数外部a={a}')     #函数外部a=30

#namespace 命名空间
#命名空间指的是变量存储的位置，每个变量都需要存储到指定的命名空间中
#每一个作用域都有它对应的命名空间
#全局命名空间，用来保存全局变量。
#函数命名空间，用来存储函数中的变量
#命名空间实际上就是一个字典，是一个专门储存变量的字典。key是变量名，value是变量地址
#locals() 用于获取当前作用域的命名空间，返回一个字典。返回什么看在哪调用的
#globals() 用于获取全局作用域的命名空间，返回一个字典
#

scope = locals()
print(scope,)   #节选：{'__name__': '__main__', '__doc__': None, '__
#向scope中添加一个k-v对，看是不是等同于创建了一个变量
scope['test'] = 'new var'
print(test)     #new var   虽然ide报错，但执行得出结果。思路没错但不建议这么做。






