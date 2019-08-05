#类似设计模式的Decoration

def add(a, b):
    return a+b

def mul(a,b):
    return a*b

#希望函数执行前，打印“开始计算”；执行完后，打印“计算完毕”
#显然在函数里+print语句是不好的，又麻烦，又破坏OCP
#那么装饰工厂就该出来干活了

def begin_end(old):
    '''
    用于对旧函数进行装饰
    :param old: 被装饰的函数
    :return:
    '''
    def new_func(a, b):
        print('开始计算')
        #调用被装饰的函数
        ans = old(a, b)
        print('ans =',ans)
        print('计算完毕')
    return new_func     #注意，这个返回函数，是用函数名返回的。有()的话运行报错

new_add = begin_end(add)
new_add(10,15)
#开始计算
#ans = 25
#计算完毕

#一般会写的更普及化，上面例子接受参数就挺麻烦的，不能多不能少，普适性不好
def common_begin_end(old):
    '''
    用于对旧函数进行装饰
    :param old: 被装饰的函数
    :return:
    '''
    def new_func(*args, **kwargs):
        '''
        传入的函数，处理参数
        :param args: 用 * ，接受位置参数。tuple嘛，就是序列
        :param kwargs:  用 ** ，接受关键字参数。dict嘛，就是键值对
        :return:
        '''
        print('开始执行')
        #调用被装饰的函数
        old(*args, **kwargs)  #将参数拆包传进去
        print('执行完毕')
    return new_func

#在定义的函数上面，  @装饰器   会将其作用到函数上
# 然后用函数名调用就会调用添加了装饰器的函数

@common_begin_end       #装饰器就是这么用的
def sayhello(name):
    print(f'Hello,Nice to meet you,{name}')

sayhello('fzf')
#开始执行
#Hello,Nice to meet you,fzf
#执行完毕

#一个函数，可以多个装饰器一起作用，无非就是多几行 @装饰器
#装饰器逐次产生作用，顺序是根据离函数的远近，从近到远依次执行
def dec0(old):
    '''
    用于对旧函数进行装饰
    :param old: 被装饰的函数
    :return:
    '''
    def new_func(*args, **kwargs):
        '''
        传入的函数，处理参数
        :param args: 用 * ，接受位置参数。tuple嘛，就是序列
        :param kwargs:  用 ** ，接受关键字参数。dict嘛，就是键值对
        :return:
        '''
        print('dec0装饰开始')
        old(*args, **kwargs)  # 将参数拆包传进去
        print('dec0装饰结束')
    return new_func

@dec0
@common_begin_end
def fun0():
    print('我是被装饰的原始函数，我执行了')

fun0()
#dec0装饰开始
#开始执行
#我是被装饰的原始函数，我执行了
#执行完毕
#dec0装饰结束