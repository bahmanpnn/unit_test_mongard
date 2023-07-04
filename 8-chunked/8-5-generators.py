
"""
    generator is a new easy way to make iterables obj's and it uses in big data's using.
    for example if we want too return 3 data and obj from many of data;its bad,
    to use list comperhension or other ways.so we can use generators to,
    every time we need to their data call them to return it!!

    generator ==> 1-function ,2-expression(comperhension)!=list comperhension
"""

#normal function
def show1():
    return 'this is show1'

print(show1())

#function generator
def show2():
    yield 'this is show2'
    yield 'hellooooooo'

print(show2())
# printing generators just can see obj and saving location in memory
# <generator object show2 at 0x0000017433154350>
#  but if try too use loop in generators we can see items that returned with yield!

for i in show2():
    print(i)


print('-------------------------')
#example 2

def show(num):
    print('starting')
    while(num>0):
        yield num
        num-=1


print(show(5))
for item in show(5):
    print(item)

print('------')
s=show(3)

print(next(s))
print(next(s))
print(next(s))



print('-------------------------')
#example3 expression(comperhension)
# expressions are like list comperhensions witout brackets!

even_numbers=[numbers for numbers in range(1,11) if numbers%2==0]
even_numbers_expression=(number for number in range(1,11) if number %2==0)

print(even_numbers)
print(even_numbers_expression)

print('-----')
for item in even_numbers_expression:
    print(item)


#we cant use loops in expression with range but we can use next for them un loops!!
# for j in range(1,11):
#     print(even_numbers_expression[j])

# print(even_numbers_expression[:3])

n=0
while(n<3):
    print(even_numbers[n])
    n+=1

while (n<3):
    print(next(even_numbers_expression))
    n+=1