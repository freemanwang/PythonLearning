# while循环

#for循环
#for 可以结合range()实现范围控制

#记不同。python中循环可以配合else，执行完循环后，会执行else
i= 0
while i < 3:
    print(i)
    i+=1
else:
    print("循环结束")
#0 1 2输出后，再输出 ”循环结束“

#break 和 continue 和其他语言也没什么区别
# 关键点在如果用break跳出循环，那么else不会执行
for i in range(5):
    if i ==3:
        break
    print(i)
else:
    print("循环结束")
#仅输出：0 1 2

#pass 语句
#pass是空语句，不做任何事。仅用于占位，比如说给后续添加功能留地方，或者等待键盘中断(ctrl+c)
while True:
    pass  #等待键盘中断

