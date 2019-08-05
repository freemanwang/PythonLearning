#Package  包
#包也是一个模块
#当模块中代码过多时，或一个模块要被分为多个模块时，就需要用到包
#包就是一个文件夹


#包中必须要有一个 __init__.py  文件，这个文件中可以包含包中的主要内容
#包中可以放其他模块
import package

print(package)  #<module 'package' (namespace)>
print(package.a)    #10

from package import m1
print(package.m1.name)  #This is form moudle a in package
#PS:没有14行，仅有9行，第15行会报错

# __pycache__  是模块的缓存文件
#py代码在执行前，需要被解析器转换为机器码，然后执行
#模块在使用时，也需要先转为机器码再执行
#为提高性能，python在编译过一次后，会将代码保存到一个缓存文件中
#这样下次加载这个包时，从缓存中读，提高性能

#实际去项目根目录OOP文件夹下，的确存在 __pycache__文件夹，
#文件夹内部有 extern_test_moudle.cpython-37  文件