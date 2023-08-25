from mysql.connector import connect, cursor, pooling
import os

cnx_pool = pooling.MySQLConnectionPool(
    pool_name = "test",
    pool_size = 5,
    pool_reset_session = True,
    host = "localhost",
    user = "root",
    password = os.environ.get("dbpassword"),
    database = 'website'
)

#1
connection  = cnx_pool.get_connection()
cursor = connection.cursor()
select_string = "select * from member where name = %s"
condition = ('Bob',)
cursor.execute(select_string, condition)
result = cursor.fetchall()
print(result)
connection.close()

#2
connection  = cnx_pool.get_connection()
cursor = connection.cursor()
select_string = "select * from member where name = %s"
condition = ('Carl',)
cursor.execute(select_string, condition)
result = cursor.fetchall()
print(result)

#3
connection  = cnx_pool.get_connection()
cursor = connection.cursor()
select_string = "select * from member where name = %s"
condition = ('Mark',)
cursor.execute(select_string, condition)
result = cursor.fetchall()
print(result)

#4
connection  = cnx_pool.get_connection()
cursor = connection.cursor()
select_string = "select * from member where name = %s"
condition = ('David',)
cursor.execute(select_string, condition)
result = cursor.fetchall()
print(result)

#5
connection  = cnx_pool.get_connection()
cursor = connection.cursor()
select_string = "select * from member where name = %s"
condition = ('Test4',)
cursor.execute(select_string, condition)
result = cursor.fetchall()
print(result)

#6
connection  = cnx_pool.get_connection()
cursor = connection.cursor()
select_string = "select * from member where name = %s"
condition = ('Test5',)
cursor.execute(select_string, condition)
result = cursor.fetchall()
print(result)
