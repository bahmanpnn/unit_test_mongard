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
