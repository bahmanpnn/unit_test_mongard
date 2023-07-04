"""
    https://www.mongard.ir/one_part/15/python-iterate/
    
    iterable,iterator,itaration ==iterate
    __iter__,__next__
    
    To convert an iterable object into an iterator, we use iter() in python. The python iter method creates and returns an iterator object.
    The syntax of the method iter in python is: iter(object, sentinel). The object parameter is required, but the sentinel parameter is optional.
    The sentinel value is a special value that stores the end of the sequence.
    If the sentinel value is provided, then the iter() method returns an iterator until the sentinel value is not reached.
    If the object provided as parameter is a user-defined object then the object must implement __iter__() method and __next__() or __getitem__() method otherwise the TypeError exception is raised by the iter in python.

"""

# for i in range(10): # ==>iteraton
#     print(i)

#example2

# for i in 'bahman':
#     print(i)

# for i in 123:
#     print(i) ==> it has error becase 123 is not iterable

#example3
class Friend:
    def __init__(self):
        self.names=['ali','amir','reza','asghar']

    def __iter__(self):
        return iter(self.names)

    # def __iter__(self):
    #     for name in self.names:
    #         yield name

f=Friend()
print(f)
print(list(f))

# l=[]
# for x in f:
#     l.append(x)

# print(l)


# example 4
# iterators are like iterables but they have diffrence.iterables return all member one at a time 
# but iterators stream a data and return apart of members at a time and send all member in a some times

#for changing e class(iterable?) to iterator we must use __next__ method in that!!
#remember that after returneing all members in iterators must raise stopiterator

class Friend_two:
    def __init__(self):
        self.names=['ali','amir','reza','asghar']

    # def __iter__(self):
    #     return iter(self.names)

    def __iter__(self):
        for name in self.names:
            yield name

    def __next__(self):
        names_copy=self.names
        if names_copy:
            return names_copy.pop()
        else:
            raise StopIteration

# f=Friend_two()

# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))


#example 5
class Friend_three:
    def __init__(self):
        self.names=['ali','amir','reza','asghar']

    # def __iter__(self):
    #     return iter(self.names)

    def __iter__(self):
        self.names_copy=self.names
        return self

    def __next__(self):
        if self.names_copy:
            return self.names_copy.pop()
        else:
            raise StopIteration



# u=Friend_three()
# o=iter(u)
# print(iter(o))
# print(iter(o))
# print(iter(o))
# print(iter(o))


print('------------------------')
#extras ***

#example6

numbers = [(1, 2, 3, 4, 5)]
iterator_object = iter(numbers)
print(type(iterator_object))

# list of numbers
numbers = [1, 2, 3, 4, 5]
iterator_object = iter(numbers)

for i in range(len(numbers)):
    print("Index:", i, "--> Value: ", next(iterator_object))

#example7
class Numbers:
    def __init__(self, max_number):
        self.maximum_number = max_number

    # need to implement __iter__() method for custom classes.
    def __iter__(self):
        self.number = 0
        return self

    # need to implement __next__() method or __getitem__() method for custom classes.
    def __next__(self):
        self.number += 1
        return self.number

number_object = Numbers(3)

iterator_object = iter(number_object)
print(next(iterator_object))
print(next(iterator_object))
print(next(iterator_object))

#8
class TwiceNumber:
    def __init__(self):
        self.current_number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_number = self.current_number * 2
        return self.current_number

    # Calling method
    __call__ = __next__
    
iterator_object = iter(TwiceNumber(), 32)

for i in iterator_object:
    print(i)
