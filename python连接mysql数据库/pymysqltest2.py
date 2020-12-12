import pymysql

#打开数据库连接，不需要指定数据库，因为需要创建数据库
conn = pymysql.Connect(
    "localhost",
    "root",
    "root"
)

#获取游标
cursor = conn.cursor()

#创建数据库(pythondb)
res = cursor.execute("CREATE DATABASE IF NOT EXISTS pythondb DEFAULT CHARSET utf8 COLLATE utf8_general_ci;")
print("create database pythonDB, res is %d" %res)

#先关闭游标，再关闭数据库连接
cursor.close()
conn.close()

#打开数据库连接
conn = pymysql.Connect(
    "localhost",
    "root",
    "root",
    "pythondb"
)

#获取游标
cursor = conn.cursor()

#创建表(user)
cursor.execute("drop table if exists user")
sql="""CREATE TABLE IF NOT EXISTS `user` (
	  `id` int(11) NOT NULL AUTO_INCREMENT,
	  `name` varchar(255) NOT NULL,
	  `age` int(11) NOT NULL,
	  PRIMARY KEY (`id`)
	) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""

res = cursor.execute(sql);

print("create table user, res is %d" %res)

#插入单条数据
insert = cursor.execute("insert into user values(1,'tom',18)")
print('添加语句受影响的行数：', insert)

#另一种插入数据的方式，通过字符串传入值
sql = "insert into user values(%s, %s, %s)"
insert = cursor.execute(sql, (3, 'jerry', 20))
print('添加语句受影响的行数：', insert)

#批量插入多条数据
#另一种插入数据的方式，通过字符串传入值
sql = "insert into user values(%s, %s, %s)"
insert = cursor.executemany(sql, [(4, 'wen', 20), (5, 'tom', 10), (6, 'test', 30)])
print('批量插入返回受影响的行数：', insert)

#查询数据
#使用execute()函数得到的只是受影响的行数，并不能真正拿到查询的内容。
#cursor对象还提供了3种提取数据的方法：fetchone、fetchmany、fetchall。
#每个方法都会导致游标动，所以必须注意游标的位置。
cursor.execute("select * from user;")
while 1:
    res = cursor.fetchone()
    if res is None:
        #表示已经取完结果集
        break
    print(res)

cursor.execute("select * from user;")
resTuple = cursor.fetchmany(3)
print(type(resTuple))
for res in resTuple:
    print(res)

cursor.execute("select * from user;")
resTuple = cursor.fetchall()
print(type(resTuple))
print("一共%d条数据" %len(resTuple))
for res in resTuple:
    print(res)

#更新数据

#先关闭游标，再关闭数据库连接
cursor.close()
conn.commit()
conn.close()