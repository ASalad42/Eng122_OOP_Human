# Human OOP

![](https://github.com/ASalad42/Eng122_OOP_Human/blob/main/humandiagram.PNG)

## keywords 
`pass` 
- When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed. 
- Empty code is not allowed in loops, function definitions, class definitions, or in if statements. 

`super()` 
- function is used to give access to methods and properties of a parent or sibling class.
- super() function will make the child class inherit all the methods and properties from its parent

`__init__(self):` 
- All classes have a function called __init__(), which is always executed when the class is being initiated. 
- Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created
- __init__ to declare class attributes
- The __init__() function is called automatically every time the class is being used to create a new object.

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
        pass # nothing happens 

    def attend_meetings(self):
        return "only on wednesdays and Fridays"


female_object = Female()

#print(female_object.work())
#print(female_object.run())

print(female_object.send_email())

````



