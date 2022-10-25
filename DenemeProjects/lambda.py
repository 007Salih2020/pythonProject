# lambad is used for anonymous functions

# lambda arguments : expression

calc = lambda num: "even number" if num % 2 == 0 else "Odd number"

print(calc(19))

# lambda properties

string = "LovelyWiesbaden"

print(lambda string: string)

# lambda return value

filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit])
print("filter_nums():", filter_nums("Wiesbaden107"))

do_exclaim = lambda s: s + '!'
print("do_exclaim():", do_exclaim("I have fun"))

find_sum = lambda n: sum([int(x) for x in str(n)])
print ("find_sum(): ", find_sum("107"))

# difference between lambda and function

def cube(y):
    print(f"Finding cube of number:{y}")
    return y*y*y
lambda_cube = lambda num: num **3

print("invoking function defined with def keyword:")
print(cube(30))

print("invoking lambda function: ", lambda_cube(30))

#  lambda function inside another function

l=["1","2","3","4","5","-1","-2","0"]

print("Sorted numerically:",
      sorted(l, key= lambda x: int(x)))

print("Filtered positive even numbers:",
      list(filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0), l)))

print("Operation on each item using lambda and map()",
      list(map(lambda x: str (int(x) + 10), l)))

