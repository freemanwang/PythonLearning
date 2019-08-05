# input([str])  用于获取用户的输入
#调用后，执行暂停，等待用户输入；
#用户输入完内容后，enter，方继续执行
#用户输入的内容以字符串 str 类型返回值得形式返回
#可以设置一个字符串做参数，做执行时得提示

# username = input("pls input username：")
# if username == 'admin':
#     print('欢迎管理员登陆')
# else:
#     print(f'欢迎{username}登陆')

#需要其他类型，比如整数，那就输入再转型
age = input("pls input your age:")
try:
    age = int(age)
    print("you are %d years old."%age)
except ValueError: 
    print("error input!")
finally:  #不论有无异常，一定执行，类似java
    input("ENTER to exit")





