# inherit everything from Human class into male

# how to import from another file in python
from human import Human

class Male(Human): # parent class (Human) is the base super class
    def __init__(self): # __init__ to declare class attributes

        # this lets the program know to inherit everything from parent class
        super().__init__() # super is used to inherit everything from base class
        self.working = True
        self.has_womb = False
        self.has_long_hair = False

    def work(self):
        return "works full time"

    def send_email(self):
        return "sends emails automically"

    def attend_meetings(self):
        return "only on mondays and tuesdays"


male_object = Male()

print(male_object.attend_meetings())
print(male_object.sleep())