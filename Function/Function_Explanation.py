#help()是python的内置函数，可用于查看python函数的用法
#语法：help(func)

#help(print)   #显示了一大堆

def maxInTwoNumbers(a:int, b:int) ->int:
    '''
    函数用于求出2个数字中，谁更大。执行函数后较大者会作为返回值。
    :param a:
    :param b: 一个数字
    :return: a，b中的较大者
    '''
    if a > b:
        return a
    else:
        return b

help(maxInTwoNumbers)
#PS：help()的参数是函数名，意思是，别跟()，否则就是help(返回值)了
#打印出的内容如下：

#maxInTwoNumbers(a: int, b: int) -> int
#    函数用于求出2个数字中，谁更大。执行函数后较大者会作为返回值。
#    :param a:
#    :param b: 一个数字
#    :return: a，b中的较大者