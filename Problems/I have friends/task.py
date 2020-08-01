class User:
    def __init__(self, username):
        self.username = username
        self.friends = 0

    def add_friends(self, n):
        self.friends += n
        print(f"{self.username} now has {self.friends} friends.")
