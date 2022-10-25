#
def f():
    s= " I love Wiesbaden"
    print(s)

f()

#
def f():
    print("Inside Function", s)

s= "I love Frankfurt too"
f()
print("Outside Function", s)

# function with variable  s

def f():
    s=" Me too"
    print(s)

s= "I love Wiesbaden"
f()
print(s)
print("\n{s}")
# function uses global variable s

# global variable 's'

def f():
    global s
    s += 'ILW'
    print(s)
    s= "I love Wiesbaden esp Kurpark"
    print(s)
# Global scope
s= "Kurpark is very beautiful"
f()
print(s)

# using global & local variables
a = 1
def f():
    print('Inside f(): ', a)
def g():
    a = 2
    print('Inside g():', a)
def h():
    global a
    a = 3
    print('Inside h():', a)

# global scope
print('global:', a)
f()
print('global:', a)
g()
print('global:', a)
h()
print('global:', a)
#