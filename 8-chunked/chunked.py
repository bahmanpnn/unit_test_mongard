"""
# islice(iterable,stop)
# islice(iterable,start,stop)
# islice(iterable,start,stop,step)

"""
from itertools import islice
from functools import partial

l=[1,2,3,4,5,6,7,8]

def take(iterable,n):
    return list(islice(iterable,n))


# print(take(l,3))
# print(list(iter(take(l,3))))

def chunked(iterable,n,strict=False):
    def ret():
        for chunk in iterator:
            if len(chunk)!=n:
                raise ValueError('iterator is not divisible by n!!')
            yield chunk

    # iterator=partial(take,iter(iterable),n)==>[1,2,3]
    iterator=iter(partial(take,iter(iterable),n),[]) #==>[1,2,3],[4,5,6],[7,8]
    
    # if n is None:
    #     raise ValueError('n can not be None')

    if strict:
        if n is None:
            raise ValueError('n can not be None when strict is True!!')
        
        return iter(ret())
    else:
        return iterator
    

# print(list(chunked(l,None,strict=True)))
# print(list(chunked(l,3,strict=True)))
print(list(chunked(l,3)))
