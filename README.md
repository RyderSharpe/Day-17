# CLASS #########
class Dog:
    pass

######### ATTRIBUTES #########
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object of the Dog class
my_dog = Dog("Buddy", 3)

# Accessing attributes
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3

######### METHODS #########
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof! Woof!")

# Creating an object of the Dog class
my_dog = Dog("Buddy", 3)

# Calling the method
my_dog.bark()  # Output: Woof! Woof!

######### FUNCTIONS #########
def greet(name):
    print("Hello,", name)

# Calling the function
greet("Alice")  # Output: Hello, Alice

######### OBJECTS #########
class Dog:
    def __init__(self, name):
        self.name = name

# Creating objects of the Dog class
dog1 = Dog("Buddy")
dog2 = Dog("Max")

# Accessing object attributes
print(dog1.name)  # Output: Buddy
print(dog2.name)  # Output: Max
