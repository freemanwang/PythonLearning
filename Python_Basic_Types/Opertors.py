#运算符
#简单的不说了

#python中，字符串可以直接用  >   <  进行比较，内部逻辑和其他语言一样,不一定比完，比出个大小即可
#实际比较的是字符串的Unicode编码
str1 = 'abc'
str2 = 'ABC'
if str1 > str2:
    print(str1 + '>' + str2)
else:
    print(str1 + '<' + str2)
#abc>ABC

#  ==   !=  可用于判断对象是否相等，比的是对象的value是否相等
#上句的值是指内存中对象的value，非变量名的value（对象id）
o1 = [1,2,3]
o2 = [1,2,3,4]
print(o1[1] == o2[1])  #True
print(o1[1] == o2[2])  #False

# is 和 is not  比较的是对象的id，即是否是同一对象
#我们可以用  id(x) == id(x2)
print(o1[1] is o2[1]) #True
print(o1[0] is not o2[0])   #False
print(id(o1[1]),id(o2[1]))  #140706275976048 140706275976048 惊了，地址竟然一样，真省成本
o2[1] = 5
print(id(o1[0]),id(o2[0]))  #140706275976016 140706275976016 相同部分还是一样
print(id(o1[1]),id(o2[1]))  #140706275976048 140706275976144 不同部分地址就不一样了
print(id(o1[2]),id(o2[2]))  #140706275976080 140706275976080 这也太狠了，到下一个相同就又共用了


#逻辑运算符
#非布尔值进行与或运算时，python会将其当bool运算，最终返回原值
#返回谁，根据与或进行判断
# 与的话，前为False会屏蔽后，直接返回False；前为True则返回后；
# 或的话，前对True会屏蔽后，直接返回前；否则返回后
#and
print( True and False)  #False
print( 1 and -1)  #-1  但被当作True
#依据是下面输出的是  True
if ( 1 and -1):
    print(True)
else:
    print(False)
print( 'abc' and -1)  #-1  等价True

#not
#对bool取反
#非bool型，先转成bool，再取反
print(not 1)    #False
print(not 'abc')    #False
print(not None)     #True


#or
print(1 or 0)  #1
print(0 or 1)  #1
print(0 or 0)  #0
print('abc'  or 1)  #abc