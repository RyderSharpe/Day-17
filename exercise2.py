class User:

    def __init__(self, user_id, username): # __init__ is called everytime you create a new object from this class
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0



user_1 = User("001", "Ryder")
print(user_1.username)

user_2 = User("002", "Heidi")
print(user_2.username)

print(user_1.followers)