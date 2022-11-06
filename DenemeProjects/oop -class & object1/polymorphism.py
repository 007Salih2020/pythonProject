# many forms
# same function but different signatures

# len() being used for a string
print(len("Wiesbaden"))

# len() being used for a list
print(len([10, 20, 30]))

print("_ _ _ _  _  _")
# example of polymorphism

def add(x, y, z = 0):
    return x+y+z

# drriver code

print(add(2, 3))
print(add(2, 3, 4))

print("_ _ _ _  _  _")
# example of polymorphism with class methods

class Germany:

    def capital(self):
        print("Berlin is the capital city of Germany. ")

    def language(self):
        print("German is the official language of Germany")

    def type(self):
        print("Germany is developed country ")

class Romania:

    def capital(self):
        print("Bükres is the capital city of Germany. ")

    def language(self):
        print("Romanian is the official language of Germany")

    def type(self):
        print("Romania is developing country ")

obj_germ = Germany()
obj_romn = Romania()

for country in (obj_germ, obj_romn):
    country.capital()
    country.language()
    country.type()


print("- - - - - - ")

#  Polymorphism with Inheritance

class Bird:

    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot")

class sparrow(Bird):

    def flight(self):
        print("Sparrow can fly")

class ostrich(Bird):

    def flight(self):
        print("Ostrich cannot fly !")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()


print(" - - - - -  -")

#  Polymorphism with function and objects

def func(obj):

    obj.capital()
    obj.language()
    obj.type()

obj_germ = Germany()
obj_romn = Romania()

func(obj_germ)
func(obj_romn)

print(" - - - - -  -")

#