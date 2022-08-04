# inherit everything from Human class into female

# how to import from another file in python
from human import Human

class Female(Human): # parent class (Human) is the base super class
    def __init__(self): # __init__ to declare class attributes

        # this lets the program know to inherit everything from parent class
        super().__init__() # super is used to inherit everything from base class
        self.working = True
        self.has_womb = True
        self.has_long_hair = True

    def work(self):
        return "works part time"

    def send_email(self):
        return "sends emails manually"

    def attend_meetings(self):
        return "only on wednesdays and Fridays"


female_object = Female()

print(female_object.work())
print(female_object.run())

