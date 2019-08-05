#递归求阶乘
def recur(num):
    '''
    递归计算传入整数的阶乘并返回
    :param num:求阶乘的整数
    :return: num!
    '''
    if num == 1:
        return 1
    return num*recur(num-1)

ans = recur(10)
print(ans)  #3628800  正确的

#递归求字符串是否回文
def huiwen(s:str):
    if len(s) < 2:
        return True
    elif s[0] == s[-1]:   #s[0] == s[len(s)-1]  原本这么写的，前者更好
        return huiwen(s[1:-1])  #递归检查s[1]->s[-2]。原本写的 huiwen(s[1:len(s)-1])
    else:
        return False

s = 'ababa'
print(huiwen(s))    #True
s = 'abcdefedcba'
print(huiwen(s))    #True
s = 'helloworld'
print(huiwen(s))    #False




