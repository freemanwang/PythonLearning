#python有自动的垃圾回收机制，会自动将没有被引用的对象删除，因此不需要手动处理垃圾回收
#

class A:
    def __init__(self):
        self.name = 'A类'

    # __del__()是一个特殊方法，它会在对象被垃圾回收前调用
    def __del__(self):
        print("A对象被删除了",self)

a = A()
print(a.name)
a = None    #A对象被删除了 <__main__.A object at 0x0000028AACC1DA20>
#a指向None时，A类在内存中的对象没有被引用，因此被删除了
