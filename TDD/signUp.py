class SignUp():
    def __init__(self):
        self.user_bio = dict()
    def add(self, username, password):
        self.user_bio[username] = password
    
    def get_password(self, username):
        return self.user_bio[username]
    
    def length_of_bio(self, username,password):
        self.user_bio[username] = password
        return  