
"""

functools ==> 1.partial ,2.update_wrapper

with partial we can use a functions in that and set args for that
args are for calling a func and method and parametrs are intrances and inputs for a method or funcs!!
---
partial can not handle dunder methods like __name__ and __doc__ so we must use update_wrapper for them

"""

from functools import partial,update_wrapper

def multi(x,y):
    return x*y

def double(x):
    return x*2

def triple(x):
    return x*3


double=partial(multi,x=3,y=2)
print('double is: ',double())


triple=partial(multi,y=3)
print('triple is: ',triple(3))

# if you print just a method and don't set any args, it act like generators and 
# see it's location in memory that obj saved!!
print('------')
print(triple)


#-------------------------
#update_wrapper

# print(double.__doc__)
# print(double.__name__)

def quadruple(x):
    """
    this is quadruple function
    """
    return x*4

# quadruple=partial(multi,x=3,y=4)
print(quadruple.__doc__)
print(quadruple.__name__)


update_wrapper(double,multi)

print(double.__name__)
print(double.__doc__)

print('-------------')
update_wrapper(multi,quadruple)
update_wrapper(triple,quadruple)

print(triple.__name__)
print(triple.__doc__)

print(multi.__name__)
print(multi.__doc__)