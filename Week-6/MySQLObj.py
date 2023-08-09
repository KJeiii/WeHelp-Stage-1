from mysql.connector import connect, cursor

class MySQLtool:
    def __init__(self, **kargs):
        self.dbhost = "localhost"
        self.dbuser = "root"
        self.dbpassword = "Jae_84265" #完成後要刪掉，改成env 
        self.database = 'website'
        self.name = kargs.get("name")  
        self.account = kargs.get("account")
        self.password = kargs.get("password")

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

    def Show_post(self):
        with connect(host = self.dbhost, user = self.dbuser, password = self.dbpassword, database = self.database) as connection:
            cursor = connection.cursor() 

            # create string for selecting data
            select_string = "select name,content from member inner join message on member.id = message.member_id"
            cursor.execute(select_string)
            data = cursor.fetchall()
            return data

    # fucntion is not completed yet!!
    def Delete_Post(self):
        with connect(host = self.dbhost, user = self.dbuser, password = self.dbpassword, database = self.database) as connection:
            cursor = connection.cursor()

            drop_string = "delete from member where id = 7"
            cursor.execute(drop_string)

# test = MySQLtool()
# print(test.Show_post())