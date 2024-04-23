class User:

    def __init__(self, user_id, username): # __init__ is called everytime you create a new object from this class
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("001", "Ryder")
# print(user_1.username)

user_2 = User("002", "Heidi")
# print(user_2.username)

user_1.follow(user_2)
print(f" user_1 has {user_1.followers} followers")
print(f" user_1 is following  {user_1.following}")
print(f" user_1 has {user_2.followers} followers")
print(f" ser_1 is following {user_2.following}")
