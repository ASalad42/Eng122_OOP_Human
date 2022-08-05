# Creating girl class

# inherit everything from Female class into girl

# how to import from another file in python
from female import Female

class Girl(Female): # parent class (Female) is the base super class
    def __init__(self): # __init__ to declare class attributes

        # this lets the program know to inherit everything from parent class
        super().__init__() # super is used to inherit everything from base class
        self.school = True
        self.parents = True
        self.toys = True

    def play(self):
        return "plays after school"

    def _study(self): # protected encapsulation
        try:
            return girl_object._study()
        except AttributeError:
            return "girl is protected at school"

    def __swims(self): # private encapsulation
        try:
            return girl_object.__swims()
        except AttributeError:
            return "where girl swims is private and hidden "

girl_object = Girl()

print(girl_object.play())
print(girl_object._study)


