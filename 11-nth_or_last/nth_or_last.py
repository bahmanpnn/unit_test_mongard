from _collections_abc import Sequence
from collections import deque
from itertools import islice

_marker=object()

def last(iterable,default=_marker):
    try:
        if isinstance(iterable,Sequence):
            return iterable[-1]
        elif hasattr(iterable,'__reversed__'):
            return next(reversed(iterable))
        else:
            return deque(iterable,maxlen=1)[-1]
    except (IndexError,TypeError,StopIteration):
        if default is _marker:
            raise ValueError(
                'last() was called on an empty iterable, and no default was provided!! '
                )
        return default
    

def nth_or_last(iterable,n,default=_marker):
    return last(islice(iterable,n+1),default=default)

l=[1,2,3,4,5]
l2=[]
print(nth_or_last(l,50))
# print(nth_or_last(l2,2))