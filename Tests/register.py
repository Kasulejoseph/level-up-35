class signUp():
    def __init__(self):
        self.fname = dict()
        self.lname = dict()
        self.emails = dict()
        
    def firstName(self,name,firstname):
        self.fname[name] = firstname
        if not isinstance(self.fname[name], str):
            raise TypeError("Value should be a string")
        if len(self.fname[name]) < 4:
            raise ValueError("name should have more than 4 characters" )
        return self.fname

    def lastName(self,name,lastname):
        self.lname[name] = lastname
        if not isinstance(self.lname[name], str):
            raise TypeError("value should be a string") 
        if len(self.lname[name]) < 4:
            raise ValueError("few character inputs" ) 
        return self.lname

    def email(self,mail,address):
        self.emails[mail] = address
        if not isinstance(self.emails[mail], str):
            raise TypeError("email should be in string format")
        if len(self.emails[mail]) < 11:
            raise ValueError("Email must have more than 10 characters " )  
    
