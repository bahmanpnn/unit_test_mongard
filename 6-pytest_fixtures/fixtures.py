class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    def fullname(self):
        return f'{self.fname} {self.lname}'
    
    def email(self):
        return f'{self.fullname()}@gmail.com'.replace(' ','')

p1=Person('bahman','pn')