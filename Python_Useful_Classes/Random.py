
import random

#def sample(self, population, k):
#Chooses k unique random elements from a population sequence or set.
#Returns a new list containing elements from the population while
#        leaving the original population unchanged.

lst = [1,2,3,4,5,6,7,8,9,10]
rd = random.sample(lst, 3)
print('从1-10中随机取3个数：',rd,'。使用的数据类型是',type(rd))
#从1-10中随机取3个数： [5, 9, 4] 。使用的数据类型是 <class 'list'>

