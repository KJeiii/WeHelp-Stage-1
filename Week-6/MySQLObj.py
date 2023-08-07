from mysql.connector import connect, cursor

class MySQLtool:
    def __init__(self, name, account, password):
        self.dbhost = "host",
        self.dbuser = "root",
        self.dbpassword = "Jae_84265", #完成後要刪掉，改成env 
        self.name = name,
        self.account = account,
        self.password = password
    
    def SignUp(self):
        with connect(host = self.dbhost, user = self.dbuser, password = self.dbpassword) as connection:
            cursor = connection.cursor()
            cursor.execute("user website")

            # create sting for adding new data
            insert_string = f"insert into member(name, username, password) values({self.name}, {self.account}, {self.password})"
            cursor.execute(insert_string)
            cursor.commit()

test = MySQLtool("test3", "123123", "123123")
test.SignUp()