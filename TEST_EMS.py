print('欢迎来到员工管理系统！')
print('请输入序号选择需要的功能（整数）:')
id = 1
header = ('员工ID'.center(4), '姓名'.center(12), '年龄'.center(6), '性别'.center(10))
#person=['1'.center(6),'Alice'.center(15),'12'.center(6),'Male'.center(14)]
#print(header[0],header[1],header[2],header[3],)
#print(person[0],person[1],person[2],person[3])
emp = []
while True:
    method = True
    while method:
        opt = input("1.添加员工  2.查询员工  3.修改员工  4.删除员工：")
        if opt not in ['1','2','3','4']:
            print('输入有误，请重新选择功能：')
        else:
            method = False
    if opt == '1':
        print('请输入员工信息')
        print('姓名,年龄(整数),性别(M(ale)/F(emale))。用英文逗号间隔开')
        inf = input('员工信息：')
        pinf = inf.split(',')
        if len(pinf)==3:
            try:
                if int(pinf[1]) in range(66) and (pinf[2] == 'M' or pinf[2] == 'F'):
                    person = []
                    person.append(str(id).center(6))
                    person.append(pinf[0].center(15))
                    person.append(pinf[1].center(6))
                    if pinf[2] == 'M':
                        sex = 'Male'
                    else:
                        sex = 'Female'
                    person.append(sex.center(14))
                    emp.append(person)
                    print(f'新员工{inf[0]}添加成功,分配员工号为 {id} 信息如下：')
                    id+=1
                    print(header[0],header[1],header[2],header[3])
                    #person = emp.pop()
                    print(person[0],person[1],person[2],person[3])
            except ValueError as err:
                print('输入有误')
        else:
            print('输入数据量不对')
    elif opt == '2':
        print('输入姓名或员工号检索员工:')
        ins = input('员工姓名/ID：')
        #print(f'输入的是{ins},类型为{type(ins)}')
        find = False
        #try:
            #if pid < 0 or pid > id:
              #  print(f'不存在id为{pid}的该员工')
           # else:
       # print(emp,'type of emp',type(emp))
        for person in emp:
            #print(person,type(person))
            for attr in person[0:2]:
                if attr.find(ins):
                    find = True
                    print(header[0], header[1], header[2], header[3])
                    print(person[0], person[1], person[2], person[3])
                    break
        if not find:
            print(f'不存在名为{ins}的该员工')
    else:
        print('待续')