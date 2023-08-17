from mysql.connector import connect, cursor
import os

class MySQLtool:
    def __init__(self, **kargs):
        self.dbhost = "localhost"
        self.dbuser = "root"
        self.dbpassword = os.environ.get("dbpassword")
        self.database = 'website'
        self.id = kargs.get('id')
        self.name = kargs.get("name")  
        self.account = kargs.get("account")
        self.password = kargs.get("password")
        self.comment = kargs.get("comment")
        self.comment_id = kargs.get("comment_id")

    def Signup(self):
        with connect(host = self.dbhost, user = self.dbuser, password = self.dbpassword, database = self.database) as connection:
            cursor = connection.cursor()

            # create string for adding new data
            insert_string = "insert into member (name, username, password) values (%s, %s, %s)"
            data = (self.name, self.account, self.password)
            cursor.execute(insert_string, data)
            connection.commit()

    def Signup_check(self):
        with connect(host = self.dbhost, user = self.dbuser, password = self.dbpassword, database = self.database) as connection:
            cursor = connection.cursor()

            # create string for selecting data
            select_string = "select count(*) from member where username = %s"
            data = (self.account,)
            cursor.execute(select_string, data)
            result = cursor.fetchall()

            if result[0][0] > 0 :
                return False
            else:
                return True
    
    def Signin(self):
        with connect(host = self.dbhost, user = self.dbuser, password = self.dbpassword, database = self.database) as connection:
            cursor = connection.cursor(dictionary=True) 

            # create string for selecting data
            select_string = "select * from member where username = %s and password = %s"
            data = (self.account, self.password)
            cursor.execute(select_string, data)
            result = cursor.fetchall()
            return result

    def Show_comment(self):
        with connect(host = self.dbhost, user = self.dbuser, password = self.dbpassword, database = self.database) as connection:
            cursor = connection.cursor(dictionary=True) 

            # create string for selecting data
            select_string = "select * from member right join message on member.id = message.member_id"
            cursor.execute(select_string)
            result = cursor.fetchall()
            return result

    def Create_comment(self):
        with connect(host = self.dbhost, user = self.dbuser, password = self.dbpassword, database = self.database) as connection:
            cursor = connection.cursor()  

        # create string for inserting data
            insert_string = "insert into message (member_id, content) values (%s, %s)"
            data = (self.id, self.comment)
            cursor.execute(insert_string, data)
            connection.commit()            
 
    def Delete_comment(self):
        with connect(host = self.dbhost, user = self.dbuser, password = self.dbpassword, database = self.database) as connection:
            cursor = connection.cursor()

            drop_string = "delete from message where id = %s"
            data = (self.comment_id,)
            cursor.execute(drop_string, data)
            connection.commit()     


    def Search_member(self):      
        with connect(host = self.dbhost, user = self.dbuser, password = self.dbpassword, database = self.database) as connection:
            cursor = connection.cursor(dictionary=True)

            # create string for selecting data
            select_string = "select * from member where username = %s"
            data = (self.account,)
            cursor.execute(select_string, data)
            result = cursor.fetchall()
            return result

    def Update_name(self):
        with connect(host = self.dbhost, user = self.dbuser, password = self.dbpassword, database = self.database) as connection:
            cursor = connection.cursor(dictionary=True)

            # update string for update name
            alter_string = "update member set name = %s where id = %s"
            data = (self.name, self.id)
            cursor.execute(alter_string, data)
            connection.commit()