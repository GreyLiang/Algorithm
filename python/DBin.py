import pymysql
import datetime

def reConnect(self):
    try:
        self.connection.ping()
    except:
        self.connection()

conn = pymysql.connect(user="root", password="password", port=3306, db="pyq", host="localhost")
cursor = conn.cursor()  # 获取游标
temp = cursor
print(conn.ping(conn))
conn.close()


# for i in range(1, 10):
#     print(cursor, temp)
#     #断线重连
#     if temp == cursor:
#         conn = pymysql.connect(user="root", password="password", port=3306, db="pyq", host="localhost")
#         print('reconnect')
#
#     #查询语句
#     sql1 = "select * from admin"
#     cursor.execute(sql1)
#     str1 = cursor.fetchall()
#     print(str1)
#     conn.commit()  # 提交事务
#
#     #打印当前时间
#     print(datetime.datetime.now())
#     temp = cursor
# conn.close()  # 关闭数据连接

'''执行sql语句灌库'''
# sqlTemp = "INSERT INTO admin VALUES (%s, %s, %s)"  # sql语句
# for i in range(1, 10):
#     print(cursor)
#     id = i
#     name = "testName" + str(i)
#     password = "testPassword" + str(i)
#     data = (id, name, password)
#     # print(sqlTemp, data)
#     cursor.execute(sqlTemp, data)  # 传  值
#     conn.commit()  # 提交事务
# conn.close()  # 关闭数据连接
