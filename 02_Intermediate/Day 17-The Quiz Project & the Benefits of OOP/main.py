class User:
    def __init__(self, user_id, username, follower=0, following=0):
        self.id = user_id
        self.username = username
        self.follower = follower
        self.following = following

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User('001', 'angela')
user_2 = User('002', 'jack')
print(user_1.follower)

user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)

i = 0
while i < 10:
    print(i)
    i = i + 1