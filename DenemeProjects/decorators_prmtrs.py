# decorators with parameters

''' 

@decorator(params)

def func_name():
 #   ''' # Function Applied '''
''


#
def decorators(*args, **kwargs):
    def inner(func):
        '''
        do operations with func
        '''
        return func
    return inner #  this is the func_obj

# @decorators(params)
def func():
    '''
    function implementation
    '''

# illustrate decorators basic in Python
def decorator_fun(func):
    print("Inside decorator")

    def inner(*args, **kwargs):
        print("Inside inner function")
        print("Decorated the function")
        # do operation with func

        func()

    return inner

@decorator_fun
def func_to():
    print("Inside actual function")

func_to()

# python code to illustrate decorators with parameters in Python

def decorator_fun(func):
    print("inside decorator")

    def inner(*args,**kwargs):
        print("Inside inner function")
        print("Decorated the runction")

        func()
    return inner

def func_to():
    print("Inside actual function")

# another way of using decorators
decorator_fun(func_to)()

# another example

def decorator(*args, **kwargs):
    print("Inside decorator")

    def inner(func):

        # code functionality here
        print("Inside * inner * function")
        print("I like", kwargs['like'])

        func()
    # returning inner function
    return inner
@decorator(like= "Wiesbaden")
def my_func():
    print("Inside actual function")

# example 3

def decorator_func(x,y):

    def Inner(func):

        def wrapper(*args, **kwargs):
            print("I like Saratoga ")
            print("Summation of values - {}".format(x+y))

            func(*args, **kwargs)

        return wrapper
    return Inner
# not using decorator
def my_fun(*args):
    for ele in args:
        print(ele)

# another way of using decorators

decorator_func(12,15)(my_fun)('I','Love','Wiesbaden')

# #  example -4
def decodecorator(dataType, message1, message2):
    def decorator(fun):
        print(message1)

        def wrapper(*args, **kwargs):
            print(message2)
            if all([type(args) == dataType for arg in args]):
                return fun(*args, **kwargs)
            return "Invalid Input"
        return wrapper
    return decorator

@decodecorator (str, "Decorator for 'stringJoin' ", "stringJoin started . . .")
def stringJoin(*args):
    st = ''
    for i in args:
        st += i
    return st

@decodecorator(int, "Decorator for 'summation'\n", "summation started . . .")
def summation(*args):
    summ = 0
    for arg in args:
        summ += arg
    return summ

print(stringJoin("I", 'Like', "Wiesbaden",'for',"History"))
print()
print(summation(19,2,8,533,67,981,119))

# #
