"""
    traceback ,print_exec(),format_exec()

    traceback use for part of some exceptions
    

    __cause__,__context__

    when python handle one error and again created another error,first one save and has 2 model.
    impicit is __context__ and we can not edit but can change __cause__
    in terminal we can see error and python handle them with __context__ and __cause__ is emmpty
    so developers can work with __cause__ for handle more errors
    **if __context__ has value __cause__ will empty and __cause__ has value __context__ will be empty
    

"""

import traceback

# print(number) ==>we didnt set this variable before so we expect to face with error
# with traceback we can handle more errors and we can check a target error in tests with traceback.format_exec()


# try:
#     print(number)
# except Exception:
#     print('error!')

# try:
#     print(number)
# except Exception:
    
#     # traceback.print_exc() ==>NoneType error
#     print(traceback.print_exc())

try:
    print(number)
except Exception:
    
    # traceback.format_exc()==> str class and error is a string
    result=traceback.format_exc()
    print(result,'\n',type(result))

print()
print('----------------------')
#__cause__ ,__context__ / 2 error at one time

# try:
#     raise ValueError('this is a value error')
# except Exception as e:
#     print('__cause__ === ',e.__cause__)
#     print('__context__ === ',e.__context__)
#     raise TypeError('this is a type error!!!') 

# try:
#     raise ValueError('this is a value error')
# except Exception as e:
#     print('__cause__ === ',e.__cause__)
#     print('__context__ === ',e.__context__)
#     raise TypeError('this is a type error!!!') from ImportError('this is from import error!!')

try:
    try:
        raise ValueError('this is a value error')
    except Exception as e:
        # print('__cause__ === ',e.__cause__)
        # print('__context__ === ',e.__context__)
        raise TypeError('this is a type error!!!')
except Exception as e2:
    print('__cause__ === ',e2.__cause__)
    print('__context__ === ',e2.__context__)

print()
print('--------------   e2')

try:
    try:
        raise ValueError('this is a value error')
    except Exception as e:
        # print('__cause__ === ',e.__cause__)
        # print('__context__ === ',e.__context__)
        raise TypeError('this is a type error!!!') from ImportError('this is from import error!!')
except Exception as e2:
    print('__cause__ === ',e2.__cause__)
    print('__context__ === ',e2.__context__)
