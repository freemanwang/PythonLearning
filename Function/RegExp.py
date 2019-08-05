#正则表达式的包是  re，  先导包
import re
word = 'am'
# ' am ' (前后有空格)出现3次，和其他字符连在一起出现2次
text = ""
file = open('poem.txt','r',encoding='UTF-8')
for line in file:
    text = text + line
# findall(pattern, string)   把所有符合的字串找出来，用list返回
res = re.findall(word,text)
print(res,len(res))     #['am', 'am', 'am', 'am', 'am'] 5

#模糊匹配，加 () 的话，返回的内容只有括号内的，虽然前面的空格也加入匹配了
ptn2 = ' *([aA][A-z]{2}) '
res = re.findall(ptn2,text)
print(res)      #除了and all 等，还有 afe，从safe里截取出来的，这不好

# 贪婪和非贪婪匹配
#   贪婪是满足情况下继续向后匹配，非贪婪是够了就停止
str1 = 'asdas235fafaghbj7832geg'
ptn1 = '[0-9]{2,5}'
ptn2 = '[0-9]{2,5}?'

print(re.findall(ptn1,str1))    #['235', '7832']  贪婪匹配
print(re.findall(ptn2,str1))    #['23', '78', '32']    非贪婪匹配

ptn3 = '\d{1,3}'
print(re.findall(ptn3,str1))  #['235', '783', '2']

string = 'http:www.baidu.com/?a=3&b=2&c=823478'
ptn = '[?](.*)'
print(re.findall(ptn,string))


# re.match(pattern, string, flags=0)  首字母开始开始匹配，string如果包含pattern子串，则匹配成功，
#   返回Match对象，失败则返回None，若要完全匹配，pattern要以$结尾。
#       group为匹配的对象，group()和group(0)为全部，后面的下标对应括号内的匹配式

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
test = re.match('ar',line)
if test:
    print(test.group())
else:
    print('ar  没匹配到')   #ar  没匹配到  注意开头，开头是Cat，和ar完全不相干，所以匹配不上
if matchObj:
    print ("matchObj.group() : ", matchObj.group()) #matchObj.group() :  Cats are smarter than dogs
    print(matchObj.group(0))    #Cats are smarter than dogs
    print ("matchObj.group(1) : ", matchObj.group(1))   #matchObj.group(1) :  Cats
    print ("matchObj.group(2) : ", matchObj.group(2))   #matchObj.group(2) :  smarter
    # print(matchObj.group(3))        #报错，no such gropu(3)
else:
    print ("No match!!")

#re.search(pattern, string[, flags])   匹配，但匹配到一个就返回，不管开头

searchObj = re.search(r'ar', line)
print(searchObj.group())    #ar
# print(searchObj.group(1)) #报错，因为search只找第一个，就停了
# print(searchObj.group(2))

#re.findall(pattern, string[, flags])  返回string中所有与pattern相匹配的全部字串，返回形式为数组。



#re.finditer(pattern, string[, flags])  返回string中所有与pattern相匹配的全部字串，返回形式为迭代器。


