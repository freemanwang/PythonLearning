# module （模块化）：指将一个完整的文件分为一个一个小的模块
#   通过模块化组合，来搭建一个完整的程序
#模块化的优点：
#   1.方便开发
#   2.方便维护
#   3.模块可以复用

#在python中，一个.py文件就是一个模块，创建模块实际上就是创建一个.py文件
#当然，模块名最好符合标识符的规范

#如何在一个模块中引入外部模块
#   1.import 模块名（模块名就是python文件名，不要.py）
#   --可以引入多次，但只会执行一次
#   2.import 模块名 as 模块别名


# import extern_test_moudle   #虽然报错但可以用
# print(extern_test_moudle)
#<module 'extern_test_moudle' from 'C:\\Users\\FZF\\PycharmProjects\\day01\\OOP\\extern_test_moudle.py'>

import extern_test_moudle  as exmoudle #虽然报错但可以用
print(exmoudle)
print(exmoudle.__name__)    #extern_test_moudle
#会打印  this is from an moudle!
#print结果和上面一样

#__name__属性值为__main__，是主模块，一个程序只有一个主模块
#主模块就是直接通过python执行的模块

print(__name__)    #__main__

#访问模块中的变量，通过 模块名.变量名
print(f"a = {exmoudle.a},b = {exmoudle.b}") #a = 10,b = 20
#访问模块中的类，通过 模块名.类名
p1 = exmoudle.Student('Alice')
print(p1.name)  #Alice


#也可以只引入模块的部分内容，
#from 模块名 import 类名, 变量名
#这样用起来，就不需要模块名前置了
from extern_test_moudle import Student
p2 = Student("Bob")
print(p2.name)  #Bob

#当然，别名依然可以用的
from extern_test_moudle import a as c
print(c)    #10

#模块内部  _变量名 只能在模块内访问，通过 imoprt * 引入时不引入这部分
#但是，直接引入模块，是可以通过  模块名._变量名  访问
from extern_test_moudle import *
#print(_inner)   #NameError: name '_inner' is not defined

import extern_test_moudle
print(extern_test_moudle._inner)    #inner


