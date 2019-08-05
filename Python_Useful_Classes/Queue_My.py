import queue
# queue 包定义了队列内容，其中有4种类型的队列
'''
一。class queue.Queue(maxsize=0)
    Constructor for a FIFO queue. maxsize is an integer that sets the upperbound limit on the number
    of items that can be placed in the queue.Insertion will block once this size has been reached,
    until queue items are consumed. If maxsize is less than or equal to zero, the queue size is infinite.
'''
'''
  应当注意的是，python中queue实现使用了多线程，后续学到线程时回顾
  当务之急，queue的put()方法有些特殊，默认情况下，队伍满会阻塞至有空位，因此向满的队伍put(),
  默认情况下不报错，但程序阻塞，不能继续向下执行。
  元素入队的2中方法：
'''
#1. Queue.put(item, block=True, timeout=None)
#   将 item 放入队列。如果可选参数 block 是 true 并且 timeout 是 None (默认)，
#   则在必要时阻塞至有空闲插槽可用。如果 timeout 是个正数，将最多阻塞 timeout 秒，
#   如果在这段时间没有可用的空闲插槽，将引发 Full 异常。
#   反之 (block 是 false)，如果空闲插槽立即可用，则把 item 放入队列，否则引发 Full 异常 ( 在这种情况下，timeout 将被忽略)。
fifoQueue = queue.Queue(3)
res = fifoQueue.put(1)
fifoQueue.put(2)
fifoQueue.put(3)
print(res)  #None
print('---------')
# fifoQueue.put(4)   //在这里会卡住，不会继续向下执行
# fifoQueue.put(4,timeout=3)    //在这里卡3S，然后报错
# fifoQueue.put_nowait(4)     #立即报错

#2. Queue.put_nowait(item)
#   相当于 put(item, False)。这样队列满时就会报错，对我来说，应该是这个方法用的多

# fifoQueue.put(4,False) //这里直接报错，raise full queue.Full
print(fifoQueue.qsize())    #3
while not fifoQueue.empty():
    print(fifoQueue.get())
#逐次输出 1  2  3
print('---------')

#队列常用方法：
#Queue.qsize()：int  返回队列大小
#Queue.e,pty()：bool  返回队列是否为空
#Queue.full():bool    返回队列是否已满
#Queue.put(obj，[block=True, timeout=None])
#       --元素入队；若队列已满，默认情况下会阻塞；设置bloack=false或者timeout过期都会报错
#Queue.put_nowait(item)   相当于 put(item, False) 。
#Queue.get(block=True, timeout=None)   出队一个元素，具体出谁看是什么队列
#Queue.get_nowait()  相当于 get(False)
que = queue.Queue(-3) # maxsize为负则队列无穷大
for t in range(100,400,100):
    que.put(t)
    print(f"{t}入队")

# i = 4
# while i > 0:
#     t = que.get()
#     print(f"{t}出队")
#     i -=1
#100 200 300依次出队，此时队伍已空但仍剩一个get()，于是阻塞，期待有什么可入队，然后再get()
#这里如果把 get() 换成 get_nowait() 就会报错

#Queue.join()  阻塞至队列中所有的元素都被接收和处理完毕。线程相关，暂且搁置
'''
二 。class queue.LifoQueue(maxsize=0)
LIFO 队列构造函数。 maxsize 是个整数，用于设置可以放入队列中的项目数的上限。当达到这个大小的时候，
插入操作将阻塞至队列中的项目被消费掉。如果 maxsize 小于等于零，队列尺寸为无限大。
'''
#理解为latest in first out 即可，其余的方法和queue没什么差别。也可以理解成栈
lifoQueue = queue.LifoQueue(3)
for t in range(1,4):
    lifoQueue.put(t)
print(lifoQueue.qsize())    #3
while not lifoQueue.empty():
    print(lifoQueue.get())
#输出的是 3  2  1，这是输入的倒序
print('---------')
'''
三。class queue.PriorityQueue(maxsize=0)
优先级队列构造函数。 maxsize 是个整数，用于设置可以放入队列中的项目数的上限。
当达到这个大小的时候，插入操作将阻塞至队列中的项目被消费掉。如果 maxsize 小于等于零，队列尺寸为无限大。
最小值先被取出( 最小值条目是由 sorted(list(entries))[0] 返回的条目)。
条目的典型模式是一个以下形式的元组： (priority_number, data) 。
'''
priorityQueue = queue.PriorityQueue(3)
priorityQueue.put(300)
priorityQueue.put(100)
priorityQueue.put(200)
while not priorityQueue.empty():
    print(priorityQueue.get())
#输出 100  200  300，看起来是最小值先被返回
print('---------')

'''
class queue.SimpleQueue
无界的 FIFO 队列构造函数。简单的队列，缺少任务跟踪等高级功能。
'''
# simpleQueue = queue.SimpleQueue()
# 很遗憾，我的py版本是3.7.2,看了下，并没有SimpleQueue。3.7.3就有
#但无关紧要，Queue已经够用了

