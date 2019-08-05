# python 对象封装，同样是隐藏对象属性，然后用getter/setter方法操作属性
#可以在属性名前加下划线，用  '_attr'来隐藏内部属性，这样在外部访问时，
# 哪怕用 instance.__attr 也无法修改之
#说是隐藏，其实是python将其变成了 _attr_ 而已，如果用 _instance._attr_ 来修改就会改变

class Person(object):
    def __init__(self, name=None, age=0):
        self._name = name  # __属性名  表示设置为只能在对象内部访问，
                            #因此在外部，使用 instance.__name 无法访问到
    def setName(self,name):
        self._name = name

    def getName(self):
        return self._name

a = Person()
a.setName('Alice')  #
print(a.getName())
a.__name = "Bob"
print(a.__name) #Bob
print(a.getName())  #Alice
#17行把 __name 改成了Bob，但是get方法出来的依然是Alice，证明没有修改到我们希望隐藏的属性
a.__Person__name_ = 'Carol'
print(a.getName())  #Alice

class Student(object):
    def __init__(self,name = None):
        self._name = name

    #property 装饰器，用来将一个get方法，转换为对象属性
    #添加property()装饰器以后，我们就可以像调用属性一样使用get方法
    @property
    def name(self):
        return self._name

st1 = Student('Alice')
print(st1.name)
#print(st1.name())   #TypeError: 'str' object is not callable,已经被当成属性而非方法了
#那么，既然是属性，我能设置值吗？
#st1.name = 'Bob'    #AttributeError: can't set attribute.一样报错
#那么，添加set方法

class Student(object):
    def __init__(self,name = None):
        self._name = name

    #property 装饰器，用来将一个get方法，转换为对象属性
    #添加property()装饰器以后，我们就可以像调用属性一样使用get方法
    @property
    def name(self):
        return self._name

    # @属性名.setter : setter方法的修饰器：
    @name.setter
    def name(self,name):
        self._name = name

st2 = Student('David')
print(st2.name) #David
st2.name = "John"
print(st2.name) #John
