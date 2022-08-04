# inherit everything from Male class into boy

# how to import from another file in python
from male import Male

class Boy(Male): # parent class (Male) is the base super class
    def __init__(self): # __init__ to declare class attributes

        # this lets the program know to inherit everything from parent class
        super().__init__() # super is used to inherit everything from base class
        self.school = True
        self.parents = False
        self.toys = False

    def play(self):
        return "plays on the weekends"

    def study(self):
        return "studies every weekday"

    def swims(self):
        return "swims every friday"


boy_object = Boy()

print(boy_object.study())
print(boy_object.send_email())