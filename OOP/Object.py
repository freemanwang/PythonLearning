#python是面向对象的
#一切皆对象
#对象就是内存中专门用来存储指定数据的一块区域
#对象实际上就是一个容器，专门用来存储数据
#之前的Number、String、Bool等都是对象

#对象的结构
#   -id（标识）：标识唯一性，在CPython中对象的内存地址，由解析器生成，可以用 id() 查看
                #CPython就是C实现的Python，最原始的Python
                #对象一旦创建，id永远不会改变
a = 123
b = 456
print(id(a),id(b))      #140706275979920 2365618152592
a = 'string'
print(id(a))        #2258274948352  变了，但这是因为不可变对象改了内容，因此指向新地址

#   -type（类型）：类型决定了对象有哪些功能
#                  python是强类型语言，一旦创建不允许改变
#                   常见类型表达如下：
print(f"type(123) = {type(123)}")       #type(123) = <class 'int'>
print(f"type(1.23) = {type(1.23)}")       #type(1.23) = <class 'float'>
print(f"type('abc') = {type('abc')}")       #type('abc') = <class 'str'>
print(f"type(Ture) = {type(True)}")       #type(Ture) = <class 'bool'>
print(f"type([1,2,3]) = {type([1,2,3])}")       #type([1,2,3]) = <class 'list'>
print(f"type((1,2,3)) = {type((1,2,3))}")       #type((1,2,3)) = <class 'tuple'>
print(f"type({1,2,3}) = {type({1,2,3})}")       #type((1, 2, 3)) = <class 'set'>
#类型转换：并不是改变对象类型，而是根据类型重新创建一个对象
#类型转换4个函数  int()  float()  str()  bool()
a = True
print('a = ', a, ',a的类型是', type(a))  #a =  True ,a的类型是 <class 'bool'>
a = int(a)
print('a = ', a, ',a的类型是', type(a))  #a =  1 ,a的类型是 <class 'int'>
#float-->int   向下取整
a = 9.99
print(f'a = {a}, int(a) = {int(a)}')    #a = 9.99, int(a) = 9
#str-->int      合法整数字符串直接转成对应数字；否则抛出异常 ValueError(小数或含字符都报错)
str = '123.456'
#print(f'str = {str}, int(str) = {int(str)}') #ValueError: invalid literal for int() with base 10: '123.456'
str = '123f'
#print(f'str = {str}, int(str) = {int(str)}')  #ValueError: invalid literal for int() with base 10: '123f'
#int-->float   与int转换基本一致
#others-->str   没啥好说的
#outhers-->bool   任何对象都可转bool，
# 任何空性对象转为False，  None、0、''(空串)、等
# 其他都转为True
a = None
print(f'a = {a}, bool(a) = {bool(a)}')    #a = None, bool(a) = False
a = 'string'
print(f'a = {a}, bool(a) = {bool(a)}')    #a = string, bool(a) = True



#   -value（值）：就是对象中存储的具体数据
                # 有些对象值是可以改变的，有些不可以
                # 对象分成2大类：可变对象、不可变对象
                #       可变对象的值可以改变（bool、list、set）
                #       不可变对象的值不可以改变（Number、str、tuple）

#变量和对象
#   内存中有个变量表，存储着已定义的变量
#   变量是一个键值对，key为变量名，value为对象id，即某内容地址
#   对象存储在内存中，变量的value（内存地址）中存的是对象的地址
a = 10
b = 10
#a,b指向同一地址
print(f'id(a)={id(a)}', f'id(b)={id(b)}')   #id(a)=140706275976304 id(b)=140706275976304
b = 20
#a指向地址不变，b指向地址发生改变
print(f'id(a)={id(a)}', f'id(b)={id(b)}')   #id(a)=140706275976304 id(b)=140706275976624





