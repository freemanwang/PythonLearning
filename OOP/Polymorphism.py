#多态是面向对象得三大特征之一
#多态使面向对象编程更具灵活性
#例如，len()函数，只要有长度，就可以在len()中用，这就是多态，不同类型都能用

#多态保证了程序的灵活性
def printName(obj):
    print(obj.name)

class Person:
    def __init__(self, name = None):
        self.name = name

class Animal:
    def __init__(self, name = None):
        self.name = name

p1 = Person('student1')
a1 = Animal('dog')
printName(p1)   #student1
printName(a1)   #dog
#如上，不同类，但只要对象有name属性，就可以使用printName方法，这就是多态