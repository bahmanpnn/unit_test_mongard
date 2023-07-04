

'''
    lambda (args):manipulate(args)
'''

def add(x,y):
    return x+y

lambda_add=lambda x,y:x+y

# print(add(2,4))
# print('--------------------')
print(lambda_add(2,4))


#--------------------------
#example2 map


x=[1,2,3,4,5,6,7,8,9]

def multi(item):
    return item**2

# print(map(multi,x)) #return object from map that we can iterate in that with for
# loop=map(multi,x)
# for i in loop:
#     print(i)

print(list(map(multi,x)))
# print('--------------------')
print(list(map(lambda i:i*i,x)))

#--------------------------
#example3 filter

def even(i):
    if i%2==0:
        return True
    return False
# print(filter(even,x)) #its return object like map too and we can iterate in that with loop
print(list(filter(even,x)))
print(list(filter(lambda i:i%2==0,x)))


#--------------------------
#example 4 sorted
y=[(4,'b'),(2,'a'),(5,'c'),(7,'e'),(1,'d')]


#this condition say that sort with second arg in tuples of list
print(sorted(y,key=lambda i:i[1])) 