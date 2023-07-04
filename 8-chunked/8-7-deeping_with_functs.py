
"""
everything(everythin that has name is class like method,functions,lists,strings,...) is class.
(blog,the history of python,2009)
----
1-funcs are objs
2-funcs can be stored in data structure(list,tuple,set,dic,...)
3-funcs can be paases to other functions(higher-order funcs)
4-funcs can be nested (inner and outer funcs)
5-funcs can capture local state(lexical closure)
6-objs can behave like funcs!

"""

#1
from typing import Any


def show(name):
    return f'hello {name}'

x=show #show here is obj and x is variable
print(x('bahman'))

#if we delete show(obj) still we can have x!but we can not call show func anymore!
del show
print(x('amir'))
# print(show('bahram'))

print('--------------------------------')
#2 we can use func in data structures because they are class!

def show_2(name):
    return f'hello {name.upper()}'

x_2=[show_2,str.capitalize,str.lower]

print(x_2) 

for i in x_2:
    print(i('bAhMAn'))

print('----')
print(x_2[1]('bahMan'))

print('---------------------------------')
#3

def shoot(func):
    return func('baHman')

print(shoot(show_2))

# shoot is higher order here(accept another func).
# there are higher order like map in python too.

for i in map(show_2,['bahaDor','BahraM','baHMAn']):
    print(i)


print('---------------------------------')
#4 nested funcs

def test():
    def test_2():
        return 'hello!!'
    
    return test_2()

print(test)
print(test())



print('------')

def show_3(name):
    def shoot(input):
        return f'Hi {input.capitalize()}'
    
    return shoot(name)

print(show_3('amIrRr'))

print('------')

#person is outer func.adult and kid is inner funcs
def person(age):
    def adult(name):
        return f'{name} is adult'
    def kid(name):
        return f'{name} is kid'
    
    if age > 18:
        return adult
    else:
        return kid
    
p=person(10)
print(p)
print(p('hamid'))

p2=person(20)('bahman')
print(p2)
    

print('---------------------------------')

# 5 inner func ha mitoonan yek seri data haro ba outer mobadele konan(bekhatere dastane parent o farzandi mese class ha)

def person2(age,name):
    """
    in this example inner funcs have access to parent parametrs(outer func parametrs)
    so we send 2 args to person2 func and it check age and then call target func!!
    adult and kid funcs has no parametr.in this example model we call them lexical closure. 

    """
    def adult():
        return f'{name} is adult'
    def kid():
        return f'{name} is kid'
    
    if age > 18:
        return adult
    else:
        return kid
    
print(person2(23,'meti'))
print(person2(23,'meti')()) 
# we must call adult / kid func.because of that must use twice ().
# first for giving args and second for calling target func.

print('---------------------------------')
#6

"""
part 1 of this ep we learned that funcs are objs.but objs are not funcs.
in this part we learn to how obj can behave like funcs!
"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f'{self.name} is {self.age} years old!!')
    

p3=Person('amir',24) #it call auto __init__ method and print last line of it
# p3() ==>we can not call obj.
# for trying to change obj to func behaviors,we can use call method for this problem

print('----------')
class Person2:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __call__(self, *args: Any, **kwds: Any):
        print(f'{self.name} is {self.age} years old!!')


p4=Person2('bahmAn',24)
p4()

