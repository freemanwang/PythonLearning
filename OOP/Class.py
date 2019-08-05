#class 类
#之前所学的都是python 内建对象，不足以满足需求
#因此开发者经常需要自定义对象。
#这没啥好说的，OOP学了挺久了，用class类去实例化instance对象

#定义类用大写字母开头，大驼峰命名法
#定义对象用小写字母开头，小驼峰命名法

#语法
#calss 类名([父类])：
#   代码块
#在类名后的括号里可以指定父类

class MyClass():
    pass

print(MyClass)  #<class '__main__.MyClass'>  意思是，在main里定义的class
mc = MyClass()  #MyClass类创造的实例对象
print(mc)   #<__main__.MyClass object at 0x0000020F5465D9B0>
print(isinstance(mc, MyClass))  #True
mc.name = 'Alice'   #mc对象里，添加了一个键值对，key='name';value='Alice'
print(mc.name)  #Alice
#当然，上述这种硬添加是不好的

#类的属性和方法
#属性：
#   在类的代码块中定义变量，将成为所有实例的公共属性
#方法：
#   对象.方法名() 调用
#   方法调用默认会传一个参数，这是和函数比起来不同的。所以方法中至少要定义一个形参
class Person():
    name = 'name'
    age = 18
    def sayHello(self):
        print("hello!")

#属性和方法查找流程
#   属性：调用一个对象属性时，解析器现在当前对象查找该属性，有就返回；没有则去
#         当前对象的类对象中查找，有则返回类对象的属性值，无则报错。

#实际上，此时内存中有Person对象，p1对象。
#Person对象的属性：name='name',方法sayHello()
#p1对象属性和方法是空的
#执行下面2个操作时，在p1对象里找不到，于是去Person对象里找，找到了name和sayHello()
p1 = Person()
print(p1.name)  #name
p1.sayHello()   #hello!

#此时p1对象有了name属性，其值为'Alice'，编译器寻找name时，先在p1中找，
#找到了该属性，就不去Person中找了。
#对象初始化时，公共属性和方法并没有在对象中实例化，多个对象共用类对象内存的属性
p1.name = 'Alice'
print(p1.name)  #Alice

class Person():
    def printMes(self):
        print(self)
    def printInfo(self):
        print(f'你好，我是{self.name}。')

p2 = Person()
p3 = Person()
print("p2地址：",p2)   #p2地址： <__main__.Person object at 0x00000282BF40A278>
p2.printMes()          #<__main__.Person object at 0x00000166AC4DA278>
print("p3地址：",p3)   #p3地址： <__main__.Person object at 0x00000282BF40A1D0>
p3.printMes()          #<__main__.Person object at 0x00000166AC4DA1D0>
#可见打印的参数是Person类的对象，实际这个默认参就是调用方法的对象自身


#在类中可定义一些特殊方法（magic），其实就是构造方法
#形式是  __方法名__   2个下划线包起方法名。这种方法在新建类时默认调用。
#构造方法不需要调用，自己会执行。
#调用类创建对象时，类后边的所有参数都会依次传递到__init()__中。

#创建对象的流程：
#   1.创建一个变量
#   2.在内存中创建一个新对象
#   3.__init__(self) 执行（如果类中存在该方法的话）
#   4.将对象的id赋值给变量

#希望在创建Person对象时，设置name属性，不设置对象将无法创建。
# 而不是新建对象后再添加name属性。这里__init()__接收到变量name后，
# 会在self中添加一个name属性，因此实际上是在对象上增加了该属性
class NewPerson():
    name = 'dafault'
    def __init__(self, name):
        print("init()执行了")
        self.name = name
        pass
    def sayHello(self):
        print(f"你好，我是{self.name}")

p1 = NewPerson('Alice')
p1.sayHello()   #你好，我是Alice


##总结

class MyClass:
    #类属性：直接在类中定义的属性是类属性
    #   类属性可以通过类或类的实例对象访问
    #   但类属性只能通过类对象来修改，无法通过实例对象修改
    classAttr = 'classAttr'

    #类方法：在类内部使用@classmethod 来修使的方法是类方法
    #类方法第一个参数是cls，也会被自动传递，cls就是当前类
    # 类方法和实例方法的区别:
    #实例方法第一个参数是self，类方法第一个参数是cls
    #类方法可以通过类调用，也可使实例调用，没区别；实例方法只能被实例调用
    @classmethod
    def clsFunc(cls):
        print('Clss Function Running!',cls)

    def __init__(self):
        #实例属性：通过实例对象添加的属性
        #   实例属性只能通过实例对象来访问和修改，类对象无法访问修改
        self.instanceAttr = 'instanceAttr'


    #实例方法：在类中定义，以self为第一个参数的方法都是实例方法
    #   实例方法在调用时，python会将调用对象作为self传入
    def test(self):
        print('Instance Function Running!',self)

    #静态方法：在类中使用@staticmethod 来修饰的方法属于静态方法
    #静态方法不需要指定任何默认参数，也不会自动传递
    #静态方法可以通过类或实例调用
    #静态函数基本上是一个和当前类无关的方法，它只是一个保存到当前类的函数
    #静态方法一般都是一些工具方法，和当前类无关
    @staticmethod
    def staticFunc():
        print('Static Funtion Running!')



cls = MyClass()
print(MyClass.classAttr)    #classAttr
print(cls.classAttr)        #classAttr
print(cls.instanceAttr)     #instanceAttr
cls.test()  #Instance Function Running! <__main__.MyClass object at 0x00000167DD79A6D8>
MyClass.clsFunc()   #Clss Function Running! <class '__main__.MyClass'>
cls.clsFunc()       #Clss Function Running! <class '__main__.MyClass'>
cls.staticFunc()