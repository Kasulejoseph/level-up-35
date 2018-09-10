class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def full_details(self):
        fullname = {
            "firstname": self.firstname ,
            "lastname": self.lastname ,
            "age": self.age
        }
        return fullname

    def description(self):
        return "{} is aged {} years".format(self.firstname,self.age)

class User(Person):
    def __init__(self,firstname,lastname,age,id,password):
        super().__init__(firstname,lastname,age)
        self.id = id
        self.password = password
    
    def full_name(self):
        user_details = super().full_details()
        us


    def setup(self):
        return "{}  password is {}".format(self.firstname,self.password)

class GuestList():
    def __init__(self,firstname,lastname,age,id,password):
        super().__init__()
        self.users = {
            "name": "kasule",
            "id": 1,
            "age": 23
        }

    def is_user_exists(self, id):
        return self.users.__contains__(id)

    def add_a_user(self,username,id):
    #    if is_user_exists(id):
    #        return "user already exists"
        if self.users["id"] == id:
            return "user already exists"
        user = User(username, "joseph", 12, id,"password123")
        self.users[id] = user

    def get_all_users(self):
        if len(self.users) ==0:
            return "no user found"
        return self.users
        
    def delete_user(self, id):
        if self.is_user_exists(id):
            return self.users
        del self.users[id]
        return self.users
        

