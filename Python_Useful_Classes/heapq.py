#堆是一个二叉树，其中每个父节点的值都小于或等于其所有子节点的值。整个堆的最小元素总是位于二叉树的根节点。python的heapq模块提供了对堆的支持。
#堆数据结构最重要的特征是heap[0]永远是最小的元素
#API:  https://docs.python.org/zh-cn/3/library/heapq.html?highlight=heapq

#API里有获取 最大/小 n个数的方法。。

'''
heapq.heappush(heap, item)¶
将 item 的值加入 heap 中，保持堆的不变性。

heapq.heappop(heap)
弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError 。使用 heap[0] ，可以只访问最小的元素而不弹出它。

heapq.heappushpop(heap, item)
将 item 放入堆中，然后弹出并返回 heap 的最小元素。该组合操作比先调用  heappush() 再调用 heappop() 运行起来更有效率。


heapq.heapify(x)
将list x 转换成堆，原地，线性时间内。


heapq.heapreplace(heap, item)
Pop and return the smallest item from the heap, and also push the new item. The heap size doesn't change. If the heap is empty, IndexError is raised.

This one step operation is more efficient than a heappop() followed by heappush() and can be more appropriate when using a fixed-size heap. The pop/push combination always returns an element from the heap and replaces it with item.

The value returned may be larger than the item added. If that isn't desired, consider using heappushpop() instead. Its push/pop combination returns the smaller of the two values, leaving the larger value on the heap.


heapq.nlargest(n, iterable, key=None)
Return a list with the n largest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower). Equivalent to: sorted(iterable, key=key, reverse=True)[:n].

heapq.nsmallest(n, iterable, key=None)
Return a list with the n smallest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower). Equivalent to: sorted(iterable, key=key)[:n].
'''

import heapq
h = []

heapq.heappush(h,5)
heapq.heappush(h,(3,'Bob'))
heapq.heappush(h,(8,'Carol'))
heapq.heappush(h,(1,'David'))

min = heapq.heappop(h)
print(min)
