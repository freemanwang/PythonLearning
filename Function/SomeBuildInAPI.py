
'''
1. enumerate(sequence, [start=0])  用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
    sequence -- 一个序列、迭代器或其他支持迭代对象。
    start -- 下标起始位置。
'''
lst = ['A','B','C','D','E']
for index,item in enumerate(lst):
    print(index,item)
'''
0 A
1 B
2 C
3 D
4 E
'''
