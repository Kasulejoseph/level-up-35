import psycopg2

class DatabaseConnection:
    def __init__(self):
        self.connection = psycopg2.connect(
        """
        dbname ='kivulu' user='postgres' password ='password'
        host='127.0.0.1' port='5432'
        """
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
    try:
        print('connected to Database')

    except Exception as e:
        print(e.message)
        print('Failed to connect to db')

    def create_user(self):
        insert_user_command = """
        INSERT INTO users(first_name,last_name,age,email,password,created_at)
        VALUES('kivumbi','ivan',30,'kvumbi@gmail.com','kivumbi123','08/09/2018')
        """
        self.cursor.execute(insert_user_command)
        self.connection.autocommit = True
    
    def update_user(self):
        pass   
    def select_user(self):
        self.cursor.execute("SELECT * FROM users")
        result = self.cursor.fetchall()
        for row in result:
            print(row)
        
