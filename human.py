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

print(person.eat())


# Polymorphism example

class Person1():
    def gender(self):
        print("this person is male")
    def main_hand(self):
        print("is right handed")

man_object = Person1()
print(man_object.main_hand())

class Person2():
    def gender(self):
        print("this person is female")
    def main_hand(self):
        print("is left handed")

women_object= Person2()
print(women_object.main_hand())