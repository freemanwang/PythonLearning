#字符串只能和字符串拼接，不能 + 其他
#字符串中可以指定占位符 %s , %s 在字符串中表任意字符
# %s 用于占位，然后 %"world" 用于去占这个位
str = "hello %s" % "world"
print(str) #hello world

#可以多个占位符，只要后面的参对应的上即可
str = "I am %s, nice to meet you, %s!" %("Alice", 'Bob')
print(str) #I am Alice, nice to meet you, Bob!

#可以用别的类型变量去填充,可以任意类型
name = 'John'
num = 123
str = 'I am %s %s' %(name,num)
print( str)     #I am John 123

#还可以格式要求,原数据占不满在前方用空格补,超了不管
str = 'Iam%5s%2s' %(name,num)
print( str)     #Iam John123

#当然，也可以限制长度在一定范围，数据从前往后打，超出位数不显示。
# 格式为 %(MinLength).(MaxLength)s,注意中间是 . 隔开上下限长
str = 'Iam%1.3s%1.2s' %(name,num)
print( str)   #IamJoh12

#Number类有专用的占位符，
# %d 整数型
# %f 浮点数占位符
# %4.2s 限制长度对留几位小数无效，所以我们用 %f 来限定小数点后留几位
a = 1234.5678
b = 12345
print('%.2f'%a)     #1234.57
print('%2.6d'%b)    #012345


#str.split(sep)        str转list，按给定字符sep分割.
str2list = 'abc,def,hjk,lmn'
arr = str.split(',')
print(arr)  #['abc', 'def', 'hjk', 'lmn']


# joint.join(arr)     list转str，数组元素间用给定字符joint连接.注意数组元素得是str，不是的话自己转
arr = [123,456,789]
i=0
while i<len(arr):
    arr[i] = str(arr[i])  #转成字符串才能拼接
    i+=1
list2str = ','.join(arr)
print(list2str) #123,456,789

#可以在字符串前添加 f 创建格式化字符串
#格式化字符串中可直接嵌入变量,变量用花括号括起来放进字符串即可
str = f'hello {a} {b}'
print(str)  #hello 1234.5678 12345

#capitalize()   将字符串的第一个字符转换为大写
#str.capitalize()
str = "hello"
print(str.capitalize())  #Hello

#center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
#如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充。
#str.center(width[, fillchar])
str = 'hello'
str1 = str.center(15)
str2 = str.center(15, '*')
print(str1)     #     hello     |这是结尾
print(str2)     #*****hello*****

#count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
#str.count(sub, start= 0,end=len(string))
str = "I am Alice "
length = len(str)
str*=3
count = str.count('Alice')
print(f'Alice 在字符串中出现的次数为{count}次')  #Alice 在字符串中出现的次数为3次
count = str.count('Alice', 0, length*2)
print(f'Alice 在字符串前2/3中出现的次数为{count}次')  #Alice 在字符串前2/3中出现的次数为2次

#endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回 True，
# 否则返回 False。可选参数 "start" 与 "end" 为检索字符串的开始与结束位置。
#str.endswith(suffix[, start[, end]])
#同理，还有个 startswith() 方法
str = 'hello world Alice'
print(str.endswith('world'))  #False
print(str.endswith('world', 0, 11))  #True
print(str.startswith('hello'))  #True
print(str.startswith('world', 6))    #True


# 重要！！
# find 和 rfind 的可选参数 beg 和 end， beg是开始下标，可以取到； end 是结束下标，娶不到。
# 而且 rfind 的下标和 find 一致，并不会出现从右往左来数 开始 和 结束 这么一说，运行得出的结论，记住了！

#find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，
# 则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，
# 返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。
# str.find(str, beg=0, end=len(string))
str = 'hello world Alice'
print(str.find('Alice'))   #12
print(str.find('Alice', 0, 10))   #-1

#rfind() 从右边开始find,其他和find()一致
#str.rfind(str, beg=0 end=len(string))
str = 'this is'
substr = 'is'
print( str.rfind(substr))      #5
print( str.rfind(substr, 0, 5))   #2
print( str.find(substr))   #2
#对比1、2的输出，可得知是从右向左检索的，但是给出的下标是从左往右数的下标

#index() 方法检测字符串中是否包含子字符串 str ，只不过如果str不在 string中会报一个异常。
#rindex() 性质一样，从右往左检索的index罢了
str = 'hello world Alice'
print(str.index('Alice'))   #12
#Traceback是python的异常，运行时检测到的错误是异常
try:
    print(str.index('John'))
except ValueError:
    print("字符串中不存在要查的子串")
#字符串中不存在要查的子串

#isalnum() 方法检测字符串是否由字母和数字组成。
#如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
#str.isalnum()
str1 = 'hello'
str2 = '123'
str3 = 'hello123'
str4 = 'hello123###'
print( str1.isalnum(), str2.isalnum(), str3.isalnum(), str4.isalnum()) #True True True False

#isalpha() 方法检测字符串是否只由字母组成。
#str.isalpha()
print( str1.isalpha(), str3.isalpha())  #True False

#isdigit() 方法检测字符串是否只由数字组成。
#str.isdigit()
print( str1.isdigit(), str2.isdigit())    #False True

#isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
str1 = 'hello123'
str2 = '987'
print(str1.isdecimal(), str2.isdecimal())   #False True

#islower() 如果字符串中包含至少一个区分大小写的字符，并且所有这些
# (区分大小写的)字符都是小写，则返回 True，否则返回 False
#isupper() 同上，不过全都的是大写的
strL = "hello"
strH = 'HELLO'
print(strL.islower(), strL.isupper())  #True False
print(strH.islower(), strH.isupper())  #False True

#isspace() 如果字符串中只包含空格，则返回 True，否则返回 False.
#str.isspace()
strNull = ''
strSP = ' '
str = 'hello world'
print(strNull.isspace(), strSP.isspace(), str.isspace())    #False True False

#istitle()  如果字符串中所有的单词拼写首字母是否为大写，且其他字母为小写则返回 True，否则返回 False.
#str.istitle()
strT = 'Hello'
print(strT.istitle(), str.istitle())    #True False

#title() 返回“标题化”的字符串，即首字母大写，其他字母小写
#str。title()
str = 'dailynews'
print(str.title())      #Dailynews

#lstrip() 返回截掉字符串左边的空格或指定字符后生成的新字符串。
#rstrip() 返回截掉字符串右边的空格或指定字符后生成的新字符串。
#str.lstrip([chars])  默认为截掉空格
#str.rstrip([chars])  默认为截掉空格
str = '********hello world********'
print(str.lstrip('*'))     #hello world********
print(str.rstrip('*'))     #********hello world

# lower() 返回将字符串中所有大写字符转换为小写后生成的字符串。
# upper() 返回将字符串中所有大写字符转换为小写后生成的字符串。
#str.lower()
#str.upper()
print(strL.upper(), strH.lower())

#swapcase() 将大写转小写，小写转大写
#str.swapcase()
str = 'HEllo'
print(str.swapcase())   #heLLO

#maketrans() 生成一个转换表，第一个参数是字符串，表示需要转换的字符，
# 第二个参数也是字符串表示转换的目标。2个字符串长度必须一致，方可一一对应。
#返回字符串转换后生成的新字符串。
#tranTab = str.maketrans(intab, outtab)
#str.translate(tranTab)
intab = 'aeiou'
outtab = '12345'
str = 'My name is Alice!'
tranTab = str.maketrans(intab,outtab)
print(str)
print(str.translate(tranTab).lstrip())   #My n1m2 3s Al3c2!

#split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num+1 个子字符串
#str.split(str="", num=string.count(str))
#参数：str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
#参数：num -- 分割次数。默认为 -1, 即分隔所有。
#返回：返回的是切分后的List，或者说数组
str = 'this is a test string'
val = str.split()
print(type(val), val)  #<class 'list'> ['this', 'is', 'a', 'test', 'string']
print(str.split('i'))  #['th', 's ', 's a test str', 'ng']   以 'i' 分割
print(str.split('i', 1))  #['th', 's is a test string']   以 'i' 分割1次





