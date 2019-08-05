#Set 集合
#同样是存储数据的结构，但和之前的存储结构们有些差异
#不同点：
#   -1.集合中只能存不可变对象
#   -2.集合中存储的对象无序（或者说不是按插入的顺序保存）
#   -3.集合中不能出现重复的元素

#创建集合，花括号即可。虽然和dict重了，但是那个是键值对，这个只存数据
s = {1, 2, 3, 4, 5, 1, 2, 3}
print(s,f'type:{type(s)}')    #{1, 2, 3, 4, 5} type:<class 'set'>  重复的并没多次存储
#什么叫只能存不可变对象（Number、str、tuple）
try:
    s = {[1,2], [3,4]}  #TypeError: unhashable type: 'list'
except Exception as e:
    print(repr(e))
#TypeError("unhashable type: 'list'")   显然，可变的list不能用set存储

#想创建一个空集合，用花括号可不行，因为那是一个dict
obj = {}
print(type(obj))    #<class 'dict'>
s = set()   #set() 方法可创建空集合
print(type(s),s)  #<class 'set'> set()

#set()同样可用于接收一个序列来创建集合
ss = set("hello world")  #用str
sl = set([1, 2, 3])     #用list
st = set((1, 2, 3))     #用tuple
sd = set({'k1':'v1', 'k2':'v2'})
print(type(ss),ss)  #<class 'set'> {'w', 'o', 'r', 'd', 'e', 'l', ' ', 'h'}
print(type(sl),sl)  #<class 'set'> {1, 2, 3}
print(type(st),st)  #<class 'set'> {1, 2, 3}
print(type(sd),sd)  #<class 'set'> {'k2', 'k1'}  注意，如果参数是dict，则只会将keys存进去
#顺带一说，虽然可变类型比如list、dict不能存进set，但这里是从list、dict里取出str类型内容存进set

#公共方法
#len(set) 看set中有多少元素
st = set('hello')
print(f'集合st中有{len(st)}个元素，分别是：{st}')
#集合st中有4个元素，分别是：{'e', 'o', 'h', 'l'}

# in 和 not in 判断元素是否在集合中
st = {'abc', 'hello'}
print(st)
print('abc' in st)  #True
print('hello' not in st)    #False


#set内置函数
#s.add(x) 添加元素x,若其已存在于set中，则无效
st = {1, 2, 3}
st.add(10)
print(st)   #{10, 1, 2, 3}

#s.remove(x)  移除元素x；若不存在则报错
st.remove(10)
#st.remove(4)    #KeyError: 4
print(st)   #{1, 2, 3}

#s.discard(x) 删除元素x，若不存在不会报错
st = {'apple', 'banana', 'cherry'}
st.discard('apple')
st.discard('dimon')
print(st)   #{'cherry', 'banana'}

#s.copy()  拷贝一个集合，返回值是拷贝的集合
stc = st.copy()
print(id(st),id(stc))   #2430631627464 2430631627688 不同，可见不是引用

#s.update(set)  修改当前集合，可以添加新的元素或集合到当前集合中
s1 = {1, 2, 3}
s2 = {'a', 'b', 1, 2}
s1.update(s2)
print(s1)   #{1, 2, 3, 'b', 'a'}

#s.intersection(set1[, set2 ...])  返回交集。
#   -set1必须，后面更多是可选
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
inter = s1.intersection(s2)
print(inter)    #{4, 5}

#s.union(set1 [, set2...])  返回并集。
s1 = {1,2,3,'a'}
s2 = {'a', 'b', 'c', 1}
un = s1.union(s2)
print(un)  #{1, 2, 3, 'a', 'b', 'c'}


#s.difference(set)  返回补集。在前者s中而不在后者set中的元素的集合
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1.difference(s2))    #{1, 2, 3}

#s.symmetric_difference() 返回 [集合的并集-集合的交集]
s1 = {1,2,3}
s2 = {2,3,4}
symmetric = s1.symmetric_difference(s2)
print('s1和s1不重复的元素为：',symmetric)    #s1和s1不重复的元素为： {1, 4}

#s.intersection_update()  在原始的集合上移除不重叠的元素。同样的，作用于s本身不返回什么
s1.intersection_update(s2)
print(s1)   #{4, 5}   在s1中去掉了不重叠的1，2，3


#s.difference_update()  在原集合上的操作，不返回。在原中移除相同的元素
s1.difference_update(s2)
print(f'操作后的s1:{s1}')   #操作后的s1:{1, 2, 3}

#s.symmetric_difference_update(set)   移除重复元素，并添加不重复元素，作用于集合，无返回
s1.symmetric_difference_update(s2)
print('(s1并s2)减(s1交s2):',s1)   #(s1并s2)减(s1交s2): {1, 4}


#s.isdisjoint(set) 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
print(f's1:{s1}\ns2:{s2}\n命题：s1与s2无重合元素。%s'%s1.isdisjoint(s2))
#s1:{4, 5}
#s2:{4, 5, 6, 7, 8}
#命题：s1与s2无重合元素。False

#注意了，判别谁是谁的子集，分清楚
#s.issubset(set) 判断s是不是set的子集，如果是则返回 True，否则返回 False。
print(s1.issubset(s2))  #True
#s.set.issuperset(set)   判断set是不是s的子集，如果是则返回 True，否则返回 False。
print(s1.issuperset(s2))    #False

#s.pop() 随机移除集合中一个元素，并将其作为返回值返回
fruit = {'apple', 'banana', 'cherry'}
print(f"pop出的元素是：{fruit.pop()}；原集合：{fruit}")
#pop出的元素是：cherry；原集合：{'apple', 'banana'}
#多次运行，pop出的内容的确会变，并非只pop最后一个










