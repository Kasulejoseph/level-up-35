import psycopg2

class DatabaseConnection:
    def __init__(self):
        self.connection = psycopg2.connect(
            """
            dbname ='dbuser' user='' password =''
            host='127.0.0.1' port='5432'
            """
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        print('connected to Database')

    except Exception as e:
        print(e.message)
        print('Failed to connect to db')

    def create_user(self, first_name, last_name, age, create_at):
        insert_user_command = """
        