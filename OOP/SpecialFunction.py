#特殊方法，也成为 magic
#特殊方法都是使用下划线 __  开头和结尾的
#特殊方法一般不需要手动调用，会在一些特殊情况下执行

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return (f"__str()__方法执行了\nPerson [name = {self.name},age = {self.age}]")


p1 = Person('Alice',12)
p2 = Person('Bob', 20)

#当我们打印一个对象时，实际上打印的是对象中特殊方法 __str()__ 的返回值
print(p1)
#__str()__方法执行了
#Person [name = Alice,age = 12]

#__repr()__