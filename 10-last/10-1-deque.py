"""
    deque just get iterable items
    
    append,appendleft,count,copy(shallow copy),clear,extend,extendleft,pop,index,append,popleft,remove,reverse,rotate
    
    maxlen does not let to add more items and everytime we want to add item remove from left(append) or right(appendleft)

"""
from collections import deque

simple_list=[1,2,3,4,5]

simple_list.append('x')
simple_list.pop(4) #pop(index)

# print(simple_list)

#deque
d=deque('amir')
# d=deque(simple_list)

# print(d)

d.append('new')
d.appendleft('left')
print(d)

print(d.count('a'))

d.extend('neww')
d.extendleft('leftt')
print(d)

d.rotate(2)
d.rotate(-2)
print(d)

print('-----------------')
dd=deque('bahman',maxlen=7)
dd.append('n')
dd.append('b')
print(dd)
dd.rotate(1)
print(dd)
