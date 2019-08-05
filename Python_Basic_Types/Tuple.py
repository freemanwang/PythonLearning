#tuple 元组
#不可变序列，多用于存储不需要改变的数据
#在操作上和list差不多，除了一些修改方法不能在其上使用，比如insert(),append()等

my_tuple = ()
print(type(my_tuple), my_tuple)

my_tuple = (1, 2, 3, 4, 5)
print(type(my_tuple), my_tuple)
print(my_tuple[1:3])
#my_tuple[2] = 'abc' #TypeError: 'tuple' object does not support item assignment

#当元组不是空元组时，新建时括号可省略。这种方法对list无效别想了
my_tuple = 1, 2, 3, 4 ,'abc', 'def'
print(my_tuple)
#如果元组不是空元组时，它里面至少要有1个逗号 ','
my_tuple = 40   #比如这里，没 , 会变成int，同理，也可以是其他比如str，bool
print(type(my_tuple), my_tuple) #<class 'int'> 40
my_tuple = 40,  #这里才是tuple
print(type(my_tuple), my_tuple) #<class 'tuple'> (40,)

#元组解包时，可以快捷操作
my_tuple = (1, 2, 3, 4)
a,b,c,d = my_tuple
print(f'a = {a}')   #a = 1
print(f'b = {b}')   #b = 2
print(f'c = {c}')   #c = 3
print(f'd = {d}')   #d = 4
#解包时，左右数量必须相等，多或少都会报错，如下2
#a,b,c = my_tuple    #ValueError: too many values to unpack (expected 3)
#a,b,c,d,e = my_tuple    #ValueError: not enough values to unpack (expected 5, got 4)

#但有时如果只需要前几个元素，不想为了取少量元素而凑一堆变量，可以这么做
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
a, b, *c = my_tuple
print(f'a={a},b={b},c={c}')     #a=1,b=2,c=[3, 4, 5, 6, 7, 8, 9]
a, *b, c = my_tuple
print(f'a={a},b={b},c={c}')
#不能有2个或更多 * 在一个语句中，会报错
#*a, *b, c = my_tuple    #SyntaxError: two starred expressions in assignment

#解包同时也可在list、str上操作
a, b, *c = [1, 2, 3, 4, 5, 6]
print(f'a={a},b={b},c={c}') #a=1,b=2,c=[3, 4, 5, 6]
a, b, *c = 'hello world'
print(f'a={a},b={b},c={c}') #a=h,b=e,c=['l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']


#交换 a 和 b 的值，这时可以利用元组的解包
a = 100
b = 200
print(a, b)     #100 200
a, b = b, a   #右侧其实是个tuple
print(a, b)     #200 100


