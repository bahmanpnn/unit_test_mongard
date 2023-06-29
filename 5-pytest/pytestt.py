
#ep3
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    def fullname(self):
        return f'{self.fname} {self.lname}'
    
    def email(self):
        return f'{self.fullname()}@gmail.com'.replace(' ','')

p1=Person('bahman','pn')

#ep4
def add(x,y):

    return x+y

def subtract(x,y):

    return x-y

def multiply(x,y):

    return x*y

def division(x,y):

    if y==0:
        raise ZeroDivisionError('can not divide by zero!!')
    
    return x/y