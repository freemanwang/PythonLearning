list = [1, 2, 3, 'a', 'b',]
str = "hello world"
itr = iter(list)
length = len(list)
i = 0
i: int

emp = [['a', 1], ['b', 2], ['c', 3]]
for p in emp:
    print('a' in p)

## 遍历
#### for可以遍历List或String
# for < variable > in < sequence >:
#     < statements >
# else:
#     <
#     statements >
# #### range( )函数
# range()
# 可以设上限、区加、步长等
# for i in range(5):  # 0<i<5
#     print(i, end=' ')
# 0 1 2 3 4

#### pass语句
# 空语句，可用于占位



## 迭代器
# 迭代器有2个基本方法，iter() 和 next()
# iter(arg)
# arg为一个List或String
# next(iter)
list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器
for i in range(4):
    print(next(it), end=' ')  # 输出迭代器下一元素
#1 2 3 4
