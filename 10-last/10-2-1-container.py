"""
    we can check one item is in one sequence or not with container and contains
    in classes must set __contains__ but main method of python hanlde auto this problem like lists
    
                        **l=[1,2,3,4] is a object of list class **
"""

listt=[1,2,3,4,5] #list is a python class and auto has __contains__ method and can check one item is in that or not!
# print(2 in listt)

class Person:
    def __init__(self,name,country):
        self.name=name
        self.country=country

p1=Person('Bahman','Iran')
# print('Iran' in p1) #person is not iterable and we get error


class Persons:
    def __init__(self,name,country):
        self.name=name
        self.country=country

    def __contains__(self,item):
        if item in self.country:
            return True
        
p2=('Bahman','Iran')
p3=('behzad','Germany')

print('Germany' in p3)