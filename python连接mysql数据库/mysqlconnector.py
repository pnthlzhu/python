"""
MySQL 是最流行的关系型数据库管理系统，如果你不熟悉 MySQL，可以阅读我们的 MySQL 教程。
本章节我们为大家介绍使用 mysql-connector 来连接使用 MySQL， mysql-connector 是 MySQL 官方提供的驱动器。
"""
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="ssms"
)

mycuror = mydb.cursor()

#mycuror.execute("SHOW TABLES")

"""
for table in mycuror:
    print(table)
"""

mycuror.execute("SELECT * FROM user")

myresult = mycuror.fetchall()

for res in myresult:
    print(res)