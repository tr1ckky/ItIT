class UserAccount:
    def __init__(self, username, email, pwd):
        self.username = username
        self.email = email
        self.__password = pwd

    def set_password(self, new_password):
        self.__password = new_password

    def check_password (self, check_password):
        return self.__password == check_password

NewUser = UserAccount("Аркадий", "arkadiyparovozov", "1235")
print (NewUser.check_password("1235"))

NewUser.set_password("3214")
print (NewUser.check_password("3214"))