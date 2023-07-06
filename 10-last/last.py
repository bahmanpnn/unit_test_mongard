from _collections_abc import Sequence
from collections import deque

_marker=object()
l=[1,2,3]
e=[]
s='bahman'

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

print(last(e,'boo'))