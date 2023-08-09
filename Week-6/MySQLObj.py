from mysql.connector import connect, cursor

class MySQLtool:
    def __init__(self, name:str, account:str, password:str):
        self.dbhost = "localhost"
        self.dbuser = "root"
        self.dbpassword = "Jae_84265" #完成後要刪掉，改成env 
        self.database = 'website'
        self.name = name
        self.account = account
        self.password = password

    def Signup(self):
        with connect(host = self.dbhost, user = self.dbuser, password = self.dbpassword, database = self.database) as connection:
            cursor = connection.cursor()

            # create string for adding new data
            insert_string = "insert into member (name, username, password) values ('{}', '{}', '{}')"
            
            cursor.execute(insert_string.format(self.name, self.account, self.password))
            connection.commit()

    def Signup_check(self):
        with connect(host = self.dbhost, user = self.dbuser, password = self.dbpassword, database = self.database) as connection:
            cursor = connection.cursor()

            # create string for selecting data
            select_string = "select count(*) from member where username = '{}'"
            cursor.execute(select_string.format(self.account))
            data = cursor.fetchall()

            if data[0][0] > 0 :
                return False
            else:
                return True
    
    def Signin(self):
        with connect(host = self.dbhost, user = self.dbuser, password = self.dbpassword, database = self.database) as connection:
            cursor = connection.cursor() 

            # create string for selecting data
            select_string = "select * from member where username = '{}' and password = '{}'"
            cursor.execute(select_string.format(self.account, self.password))
            data = cursor.fetchall()
            return data

    # fucntion is not completed yet!!
    def Delete_Post(self):
        with connect(host = self.dbhost, user = self.dbuser, password = self.dbpassword, database = self.database) as connection:
            cursor = connection.cursor()

            drop_string = "delete from member where id = 7"
            cursor.execute(drop_string)
