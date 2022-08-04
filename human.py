# creating human class

class Human:
    # __init__ to declare class attributes
    def __init__(self): #self refers to current class so Human
        self.alive = True
        self.eyes = True
        self.legs = True

    def eat(self):
        return "need to eat"

    def sleep(self):
        return "must rest"

    def run(self):
        return "have to stay fit"

# create an object of the class before using it

person = Human()

# print(person.eat())