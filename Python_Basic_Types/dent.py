# if 1 == 2:
#     print("1 == 2");
# else:
#     print("1 != 2");
#
# a = 3
# print(type(a))

# t = ['a', 'b', 'c', 1, 2]
# print(t[2])
# print(t[1:4:2])

# # set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
#
# print(a)
#
# print(a - b)  # a 和 b 的差集
#
# print(a | b)  # a 和 b 的并集
#
# print(a & b)  # a 和 b 的交集
#
# print(a ^ b)  # a 和 b 中不同时存在的元素
# dict = {}
# dict['name'] = 'Alice'
# dict['pw'] = 'root'
# print(dict)

# a = 20
# b = 20
# c = 30
# print (a is b)
# print (id(a) == id(b))
# print (a is  c)
# print (id(a) == id(c))

# a = 0
# b = 1
# c = 1
# print( a | b ^ c)

def printFib():
    a, b = 0, 1
    while b < 10:
        print (b, end=',')
        a, b = b, a+b

# printFib()
# for i in range(5):
#     print(i, end = ' ')
#
# list = [1, 2, 3, 4]
# it = iter(list)  #创建迭代器
# for i in range(4):
#     print(next(it), end = ' ')  #输出迭代器下一元素
#
# def printinfo( arg1, **vartuple ):
#    "打印任何传入的参数"
#    print ("输出: ")
#    print (arg1)
#    print (vartuple)
#
# printinfo(0,a=1, b=2)

num = 0
def outer():
    num1 = 10
    def inner():
        nonlocal num1 # nonlocal关键字声明
        num1 = 20
        print(num1)
        global num  # global声明
        num = 30
    inner()
    print(num1)
outer()
print (num)