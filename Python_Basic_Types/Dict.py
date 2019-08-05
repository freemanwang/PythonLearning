#dict 字典，或者说用键值对存储的hashtable
#dict(字典)属于一种数据结构，称之为mapping(映射)
#dict类似list，都是用来存储对象的容器
#字典中可以保存多个对象，每个对象都会有一个唯一的名字，这个名字成为key(键)
#通过key，可以快速查询value(值)
#这种存储在dict中的对象，称之为key-value(键值对)
#dict中可以有多个key-value，每一个被称为item(一项)

#使用花括号 {k1:v1, k2:v2, k3:v3.....} 创建字典


d = {}
print(f'd={d},type:{type(d)}')  #d={},type:<class 'dict'>

d = {'name':'Alice','age':12,'gender':'female'}
print(f'd={d},type:{type(d)}')  #d={'name': 'Alice', 'age': 12, 'gender': 'female'},type:<class 'dict'>
print(d.keys()) #dict_keys(['name', 'age', 'gender'])
print(d.values()) #dict_values(['Alice', 12, 'female'])

#使用dict()函数创建字典
d = dict(name='abc', age=12, gender='female')
print(d)    #{'name': 'abc', 'age': 12, 'gender': 'female'}

#dict()用双值序列做参数。即序列中只有2个值，比如[k1, v1] | (k2, v2) | 'kv' ; 甚至[(1,2),(3,4)]
d = dict([('k1','v1'), ('k2', 'v2')])
print(d)    #{'k1': 'v1', 'k2': 'v2'}

#dict的value可以是任意对象
#dict的key只能是不可变对象，且必须唯一。重复是后面的会替换掉前面的
d = {'name':'Alice','age':12,'name':'Bob'}
print(d)    #{'name': 'Bob', 'age': 12}

#根据key获取value
print(d['name'])    #Bob
print(d['age'])     #Bob
#print(d[1])     #KeyError: 1  使用了字典中不存在的key，会报错
#不确定是否有key时，为避免报错，可用get()方法，key不存在时返回None
print(d.get('name'))    #Bob
print(d.get('address')) #None

#添加
#d[key] = value  最直接的办法，问题是如果key已存在，会覆盖
# d.setdafault()  #安全些，存在就不变，没有才添加，函数中有详细
'''
    def setdefault(self, *args, **kwargs): # real signature unknown
        """
        Insert key with a value of default if key is not in the dictionary.
        
        Return the value for key if key is in the dictionary, else default.
        '''
t = d.setdefault('key',20)
print(t,d['key'],11111111111111111111111111,)

#修改
d['name'] = 'Carol'
print(d)    #{'name': 'Carol', 'age': 12}

# 删除
del d['name']
print(d)    #{'age': 12}

#公用方法

#len(dict)  计算字典中键值对个数。
d = {'name':'Alice', 'age':12, 'gender':'Female'}
print(len(d))   #3

#str(dict)  输出字典，以可打印的字符串表示。类似str(list),虽然带 {} : 等，但都是str内的字符了
print(f'type(str(d))={type(str(d))}\nstr(d):{str(d)} ')

#type(str(d))=<class 'str'>
#str(d):{'name': 'Alice', 'age': 12, 'gender': 'Female'}

#字典内置函数
#下文中，d指代实际使用时的字典名，可变；dict指代字典关键字，不可变
#d.copy()  返回dict的浅拷贝，直接在字典后跟 .copy()即可，不需要导包
#ps:既然有浅拷贝，那就会有深拷贝，深拷贝是copy.deepcopy(obj),需要import copy 后方可使用
import copy #为了使用copy对象的deepcopy()方法导的
d1 = {'user':'admin', 'file':[1, 2, 3]}
d2 = d1         #直接引用，d1的修改会影响d2，d2其实就是d1的别名
d3 = d1.copy()  #浅拷贝：拷贝父对象(一级目录)，不拷贝内部子对象
d4 = copy.deepcopy(d1)  #深拷贝：父对象及其子对象一起完全拷贝
d1['user'] = 'fzf'  #d1的一级对象'user'值改为’fzf，d2被同步影响，d3不受影响
d1['file'].remove(1)    #d1的二层对象，file内移除了元素1，d2和d3都被同步影响
print('d1:',d1)     #d1: {'user': 'fzf', 'file': [2, 3]}
print('d2:',d2)     #d2: {'user': 'fzf', 'file': [2, 3]}
print('d3:',d3)     #d3: {'user': 'admin', 'file': [2, 3]}
print('d4:',d4)     #d4: {'user': 'admin', 'file': [1, 2, 3]}

#dict.fromkeys(seq[, value])  创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
#seq -- 字典键值列表。
#value -- 可选参数, 设置键序列（seq）对应的值，默认为 None。
lst = ['name', 'age', 'gender']
tup = ('姓名', '年龄', '性别')
dic1 = dict.fromkeys(lst)
print(f'dic1:{dic1}')   #dic1:{'name': None, 'age': None, 'gender': None}
dic2 = dict.fromkeys(tup, '待补充')
print(f'dic2:{dic2}')   #dic2:{'姓名': '待补充', '年龄': '待补充', '性别': '待补充'}

#d.get(key) 函数返回指定键的值，如果值不在字典中返回默认值。
#dict.get(key [,default])
#   -key -- 字典中要查找的键。
#   -default -- 如果指定键的值不存在时，返回该默认值值。默认为None。
d1 = {'name':'admin', 'passwd':'root'}
print(d1.get('name'))   #admin
print(d1.get('level', 'No Such Attribute！'))    #No Such Attribute！

#key in dict / key not in dict   字面意思，返回bool值
print(f"'name' in d1:{'name' in d1}") #'name' in d1:True
print(f"'level' in d1:{'level' in d1}") #'level' in d1:False
print(f"'age' not in d1:{'level' not in d1}") #'age' not in d1:True

#d.keys()   返回一个元组，字典里所有的键都在里面
d = {'name':'Alice', 'age':12, 'gender':'Female'}
seq = d.keys()
print(seq, ';type:',type(seq))  #dict_keys(['name', 'age', 'gender']) ;type: <class 'dict_keys'>

#d.values()  同keys，返回的是所有的值
seq = d.values()
print(seq, ';type:',type(seq))  #dict_values(['Alice', 12, 'Female']) ;type: <class 'dict_values'>

#d.items() 返回字典的所有键值对组成的元组，可用于遍历
print(d.items(),f';type:{type(d.items())}')
#dict_items([('name', 'Alice'), ('age', 12), ('gender', 'Female')]) ;type:<class 'dict_items'>
for k_v in d.items():
    print(k_v,f';type:{type(k_v)}')
#('name', 'Alice') ;type:<class 'tuple'>
#('age', 12) ;type:<class 'tuple'>
#('gender', 'Female') ;type:<class 'tuple'>

#d.pop(key [,default])  若字典中有该key，从中删除并返回其value；否则返回dafault。
#若dafault未设置且字典中查无此key，则报KerError错
name = d.pop('name')
addr = d.pop('address', None)
print('name:%s'%name)   #name:Alice
print('address:%s'%addr)    #address:None

#popitem()  随机删除字典中一个键值对并用tuple返回key-value;一般都删除最后一个键值对
d = {'name':'Alice', 'age':12, 'gender':'Female'}
tup = d.popitem()
print(d)    #{'name': 'Alice', 'age': 12}   最后一项已删除
print(tup,type(tup))    #('gender', 'Female') <class 'tuple'>   元组类型返回key-value队


#d.setdefault(key [,dedault])
#如果key已存在于字典中，则返回对应的value，不做任何操作
#否则，添加该键值对，并设置value；default默认为None
d = {'name':'Alice', 'age':12, 'gender':'Female'}
result1 = d.setdefault('name','中国')
result2 = d.setdefault('addr', 'China')
result3 = d.setdefault('tel')
print(result1,result2,result3)  #Alice China None
# 可见119失败，返回已有value；119成功，返回了要设的值;120失败，返回None
print(d)    #{'name': 'Alice', 'age': 12, 'gender': 'Female', 'addr': 'China'}

#d.update(otherDict)    将其他字典的键值对添加进当前字典
d1 = {'a':1, 'b':2, 'c':3}
d3 = {'c':10, 'd':4}
d1.update(d3)
print(d1)   #{'a': 1, 'b': 2, 'c': 10, 'd': 4}   添加新键值对时，覆盖了重复的键值对

#clear() 猜都猜到了

