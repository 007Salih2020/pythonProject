#
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

for value in simpleGeneratorFun():
    print(value)

# generator object with next
def generatorFun():
    yield 4
    yield 5
    yield 6

x= generatorFun()

print(next(x))
print(next(x))
print(next(x))

#  Fibonacci Numbers

def fib(limit):
    a, b = 0, 1

    while a < limit:
        yield a
        a, b = b, a+b
x = fib(5)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

print("\n Using for in loop")
for i in fib(5):
    print(i)

#