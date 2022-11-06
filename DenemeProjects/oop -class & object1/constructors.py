# example default constructor

class Wiesbaden:

    # default constructor
    def __init__(self):
        self.city ="Wiesbaden"

    def print_City(self):
        print(self.city)

# creating object
obj = Wiesbaden ()

# calling the instance method using object obj
obj.print_City()

# example for parameterized constructor

class Addition:
    first  = 0
    second = 0
    third  = 0

    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First number =" + str(self.first))
        print("Second number =" + str(self.second))
        print("Addition of two numbers ="+ str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second

# creating object of the class
obj = Addition (1000, 2000)

# perform Addition
obj.calculate()

# display the result
obj.display()

#