"""
    collection.abc
    https://docs.python.org/3/library/collections.abc.html
    
    isinstance,issubclass
    Sequence,Container,Sized
"""
from _collections_abc import Sequence,Container,Sized

def one(arg1):
    if isinstance(arg1,Sequence):
        return True
    else:
        return False


# print(one(12))
# print(one('12'))
# print(one('bahman'))
print(one([1,2,3]))

print('-------------------')
# contaner(iterable)
listt=[1,2,3]
print(2 in listt)

class One:
    def __str__(self):
        pass

print('one= ',issubclass(One,Container))

class Two:
    def __str__(self):
        pass

    def __contains__(self,item):
        pass

#check contains method setted or not and class is Container 
print('Two= ',issubclass(Two,Container))

# now check instances and objects from classes to are Container(iterable) or not
a1=One()
a2=Two()

print('a1= ',isinstance(a1,Container))
print('a2= ',isinstance(a2,Container))


#Sized
print('--------------')
#check instance or class setted len method or not with Sized
class Three:
    def __str__(self):
        pass

    def __contains__(self,item):
        pass

    def __len__(self):
        return 2
    
a3=Three()

print('class Three= ',issubclass(Three,Sized))
print('a3= ',isinstance(a3,Sized))