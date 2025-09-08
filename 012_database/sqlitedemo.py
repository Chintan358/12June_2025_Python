import sqlite3

db =  sqlite3.connect("mydata.db")

# db.execute("create table student(id int primary key, name varchar(20),email varchar(30))")

# db.execute("insert into student values(2,'Krunal','krunal@gmail.com')")

# db.execute("update student set name='xyz' where id=2")

# db.execute("delete from student where id=2")

# db.commit()

# data = db.execute("select * from student")
# dt =  data.fetchall()
# for i in dt:
#    for k in i:
#       print(k)