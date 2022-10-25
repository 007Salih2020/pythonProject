# illustrate the args with extra argument

def myFun(arg1, *argv):
    print("my first argument:", arg1)
    for arg in argv:
        print("Next argument through *argv :",  arg)

myFun("Hello", "Welcome", "to", "Wiesbaden")

# passing non-keyword argument with keyword argument

def myFun(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myFun("Hi", first="Welcome", mid="to", last="Wiesbaden")

# using both *argv  & **kwargs

def mixFun(arg1, arg2, arg3):
    print("arg1 :", arg1)
    print("arg2 :", arg2)
    print("arg3 :", arg3)

args = ("welcome","to", "Frankfurt")
mixFun(*args)

kwargs ={"arg1": "welcome", "arg2": "to", "arg3": "Frankfurt"}
mixFun(**kwargs)

# using both *argv and **kwargs

def bestFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

bestFun('Welcome','to','Wiesbaden', first="Welcome", mid= "to", last= "Wiesbaden")

# using both *argv and **kwargs to set values of object

class car():
    def __init__(self, *args):
        self.speed = args[0]
        self.color = args[1]

audi=car(200, 'red')
bmw=car(250, 'black')
mb=car(190, 'white')

print(audi.color)
print(bmw.speed)

# with kwargs

class car():
    def __init__(self, **kwargs):
        self.speed = kwargs['s']
        self.color = kwargs['c']

audi = car (s=200, c='red')
bmw  = car (s=250, c= 'black')
mb   = car (s=190, c= 'white')

print(audi.color)
print(mb.speed)