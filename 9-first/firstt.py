"""
    more itertools
"""

l=[1,2,3,4,5,6,7,8]

_marker=object()

def first(iterable,default=_marker):
    try:
        return next(iter(iterable))
    except StopIteration as st:
        if default is _marker:
            raise ValueError('first() waas called on an empty iterable, and no'
                             ' default value was provided') from st
        return default
    
# print(first(l))
# print(first([]))
# print(first([],default='boo!!'))
# print(first(l,default='boo!!'))