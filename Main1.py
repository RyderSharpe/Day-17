class User:

    def __init__(self,): # __init__ is called everytime you create a new object from this class
        print("new user being created...") # evertime we create a new user, this print statement is going to be triggered.




user_1 = User()
user_1.id = "001"
user_1.username ="Ryder"
print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "Heidi"
print(user_2.username)
