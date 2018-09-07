class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def full_name(self):
        return self.firstname + " "+ self.lastname

    def description(self):
        return "{} is aged {} years".format(self.firstname,self.age)

class User(Person):
    def __init__(self,firstname,lastname,age,id,password):
        super().__init__(firstname,lastname,age)
        self.id = id
        self.password = password
    
    def ids(self):
        return self.id

    def setup(self):
        return "{}  password is {}".format(self.firstname,self.password)

class GuestList():
    def __init__(self):
        self.users = {}

    def is_user_exists(self, id):
        return self.users.__contains__(id)

    def add_a_user(self,username,id):
       if self.is_user_exists(username):
           return "not exists"
       self.users['name'] = username
       self.users['id'] = id

    def get_all_users(self):
        if len(self.users) ==0:
            return "no user found"
        return self.users

    def get_a_user_by_id(self, id):
        return self.users
        
    def delete_user(self, id):
        pass

        

