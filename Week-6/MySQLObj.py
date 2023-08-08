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
        # 研究一下這邊，為什麼用host = self.dbhost無法順利把資料傳入
        with connect(host = self.dbhost, user = self.dbuser, password = self.dbpassword, database = self.database) as connection:
            cursor = connection.cursor()

            # create sting for adding new data
            insert_string = "insert into member (name, username, password) values ('{}', '{}', '{}')"
            
            cursor.execute(insert_string.format(self.name, self.account, self.password))
            connection.commit()

    # fucntion is not completed yet!!
    def Delete_Post(self):
        with connect(host = self.dbhost, user = self.dbuser, password = self.dbpassword, database = self.database) as connection:
            cursor = connection.cursor()

            drop_string = "delete from member where id = 7"
            cursor.execute(drop_string)

