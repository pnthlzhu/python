"""
原文地址：https://www.cnblogs.com/R-bear/p/7022231.html
python DB-API介绍

1.python标准数据库接口为 python DB-API,python DB-API为开发人员提供了数据库应用标称接口
2.python数据库接口支持非常多的数据库,可以选择适合你项目的数据库:
　　MySQL
　　PostgreSQL
　　Microsoft SQL Server 2000
　　Oracle
　　Sybase
具体查看:https://wiki.python.org/moin/DatabaseInterfaces

不同的数据库,就需要下载不同的DB API模块,例如访问Oracle数据库和MySQL数据库,需要下载Oracle和MySQL数据库模块
DB-API是一个规范,它定义一个系列必须的对象和数据库存取方式,以便各种各样的底层数据库系统和多种多样的数据库接口程序提供一致的访问接口.
python的DB-API,为大多数数据库实现了接口,使用它连接各种数据库后,就可以使用相同的方式操作各种数据库

通用步骤:
1.引入模块
2.获取与数据库的连接
3.执行SQL语句和存储过程
4.关闭数据库连接

mysql登陆
基本操作：
登陆：mysql -uroot -h127.0.0.1 -P3306 -p
mysql -uroot -p(本机不用写host)
退出mysql：ctrl+z+回车，或者exit
端口号默认是3306，但是可以通过安装目录下的配置文件修改。

python3 与MySQL 进行交互编程需要安装 pymysql 库，
故首先使用如下命令安装pymysql–>pip install pymysql
"""

import pymysql

#pymysql.connect()连接数据库函数
conn = pymysql.Connect(
    "localhost",
    "root",
    "root",
    "ssms"
)

print(conn)
print(type(conn))

"""
要想操作数据库，光连接数据是不够的，必须拿到操作数据库的游标，才能进行后续的操作，比如读取数据、添加数据。
通过获取到的数据库连接实例conn下的cursor()方法来创建游标。游标用来接收返回结果
"""
#conn.cursor():获取游标
cursor = conn.cursor();
print(cursor)
#说明：cursor返回一个游标实例对象，其中包含了很多操作数据的方法，比如执行sql语句。

#执行sql语句execute和executemany
"""
注意：
1.数据库性能瓶颈很大一部份就在于网络IO和磁盘IO，将多个sql语句放在一起，
  只执行一次IO，可以有效的提升数据库性能。推荐此方法
2.用executemany()方法一次性批量执行sql语句，固然很好，但是当数据一次传入过多到server端，
  可能造成server端的buffer溢出，也可能产生一些意想不到的麻烦。
  所以，合理、分批次使用executemany是个合理的办法
"""
