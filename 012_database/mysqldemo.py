import pymysql


con =  pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    port=3306,
    database="mydb"
)

cursor = con.cursor()

# cursor.execute("create database mydb")


# cursor.execute("create table emp(id int primary key auto_increment, name varchar(20),email varchar(20))")

# cursor.execute("insert into emp values(0,'harsh','harsh@gmail.com')")


# qry = "insert into emp values(%s,%s,%s)"
# val = (0,"Krunal","krunal@gmail.com")

# qry = "update emp set email=%s where id=%s"
# val = ("kamini@gmail.com",2)

# qry ="delete from emp where id=%s"
# val = (1,)
# cursor.execute(qry,val)

# con.commit()

cursor.execute("select * from emp")
data = cursor.fetchall()

for i in data:
    print(i)


