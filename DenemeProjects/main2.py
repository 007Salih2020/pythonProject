# from jikanpy import Jikan

# jikan = Jikan()

# ternary operators
a,b = 30,20

# copy value of a in min if a < b else copy b

min = a if a<b else b

print(min)
print( (b,a) [a<b])

print( {True:a, False:b} [a<b])

print((lambda:b, lambda:a) [a<b] ())

print("both a and b are equal" if a == b else "a is greater than b"
      if a > b else "b is greater than a")