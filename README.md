# Human OOP

![](C:\Users\Ayan\PycharmProjects\human_oop\humandiagram.PNG)

## Step 1
````python
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

````

## Step 2 

````python
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

````

## Step 3

````python
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

````

## Step 4

````python
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

````

## Step 5