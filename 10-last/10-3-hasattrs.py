
"""
    hasattr,setattr,getattr,delattr
"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person('bahman',24)
print(hasattr(p1,'name'))
print(hasattr(p1,'city'))

print(hasattr(Person,'name'))
print(hasattr(Person,'city'))


class Person2:

    name='bahman'
    age=10

p2=Person2()

print('p2-name= ',hasattr(p2,'name'))
print('p2-city= ',hasattr(p2,'city'))

print('person2-name= ',hasattr(Person2,'name'))
print('person2-city= ',hasattr(Person2,'city'))

print('------------------')
#getattr
print('person2-name= ',getattr(Person2,'name'))
print('person2-age= ',getattr(Person2,'age'))

print('p2-name= ',getattr(p2,'name'))
print('p2-age= ',getattr(p2,'age'))

print('---')
print('p1-name= ',getattr(p1,'name'))
print('p1-age= ',getattr(p1,'age'))

print('-----------')
#setattr
# Person2.__setattr__(p2,'city','Tehran')
p2.__setattr__('city','Tehran')
print('p2-city= ',getattr(p2,'city'))

Person.__setattr__(p1,'city','mashhad')
print(hasattr(p1,'city'))
print(hasattr(Person,'city'))
print('p1-city= ',getattr(p1,'city'))


print('------------')
#del attr
p2.__setattr__('country','Iran')
p2.__delattr__('country')

print(hasattr(p2,'country'))
setattr(Person2,'country','Iran')
print(hasattr(Person2,'country'))
print(hasattr(p2,'country'))


# print(hasattr(p2,'country')) ==> True
# p2.__delattr__('country') ==> error!!
# delattr(Person2,'country')
print(hasattr(Person2,'country'))
