#在类创建时，类名后括号里可以写父类，该类即为父类的子类
#之前写的时候，类名后括号里都是Object，这很正常，一切类都是Object的子类


class Animal:
    def run(self):
        print('Animal can run!')

    def sleep(self):
        print('Animal can run!')

    def bark(self):
        print('Animal make noise!')

#Dog是Animal的子类
class Dog(Animal):
    def bark(self):
        print('Dog barks 旺旺~')

d = Dog()
d.run()     #Animal can run!
d.bark()    #Dog barks 旺旺~
print(issubclass(Dog, Animal))  #True
print(issubclass(Dog, object))  #True
print(isinstance(Dog, object))  #True

#方法重写
#在子类中如果有和父类同名的方法，则通过子类instance调用方法时，
# 会调用子类方法，而非父类方法。这个特点称为方法的重写（override，覆盖）
#很好理解，在子类中定义的方法，就会在子类对象的namespace中有该方法，调用时在
#自己的namespace中能找到，就不再往上找了；否则就一直向上找，以此类推，直到找到
#object，如果依然不存在，就报错。


#类名.__base__   获取当前类得所有父类
print(Dog.__base__) #<class '__main__.Animal'>
#既然说所有父类，就意味父类不止一个。
# python中支持多重继承
#但实际开发中应尽量避免多重继承，因为会使代码过于复杂
#如果子类有同名方法，那么会现在父类1中查找，找不到再去父类2中查找。。。

class A:
    def testA(self):
        print('AAA')

    def test(self):
        print('AAAAA')


class B:
    def testB(self):
        print('BBB')

    def test(self):
        print('BBBBB')


class C(A,B):
    def testC(self):
        print('CCC')


print(C.__bases__)  #(<class '__main__.A'>, <class '__main__.B'>)
c = C()
c.testA()   #AAA
c.testB()   #BBB
c.testC()   #CCC
c.test()    #AAAAA

