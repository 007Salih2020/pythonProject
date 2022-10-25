# simple yield

def simpleGeneration():
    yield 1
    yield 2
    yield 3
    yield 4

for value in simpleGeneration():
    print(value)

# generate squares from 1 to 100 using yield
def nextSquare():
    i = 1

    while   True:
        yield i*i
        i += 1

for num in nextSquare():
    if num < 100:
        break
    print(num)

#