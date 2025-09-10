from tkinter import *
from tkinter import ttk
import pymysql

con = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    port=3306,
    database="12jun_python"
)
cursor =con.cursor()

root = Tk()
root.geometry("1000x700")


def adduser():
    uname =  t1.get()
    email = t2.get()
    phone = t3.get()
    qry = "insert into student values(%s,%s,%s,%s)"
    val =(0,uname,email,phone)
    cursor.execute(qry,val)
    con.commit()
    for i in table.get_children():
        table.delete(i)
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    show()

def show():
    cursor.execute("select * from student")
    records = cursor.fetchall()
    myid = 1
    for i,(id,name,email,phone) in enumerate(records):
        # print(i)
        table.insert("","end",values=(myid,name,email,phone))
        myid+=1

id = 0
def getdata(self):
    global id
    rowid = table.selection()[0]
    data = table.item(rowid)['values']
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    id = data[0]
    t1.insert(0,data[1])
    t2.insert(0,data[2])
    t3.insert(0,data[3])

def deleteuser():
    cursor.execute(f"delete from student where id={id}")
    con.commit()
    for i in table.get_children():
        table.delete(i)
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    show()

def updateuser():
    uname =  t1.get()
    email = t2.get()
    phone = t3.get()
    qry = "update student set name=%s,email=%s,phone=%s where id=%s"
    val =(uname,email,phone,id)
    cursor.execute(qry,val)
    con.commit()
    for i in table.get_children():
        table.delete(i)
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    show()

# b1 = Button(root,text="LEFT").pack(side=LEFT)
# b2 = Button(root,text="RIGHT").pack(side=RIGHT)
# b3 = Button(root,text="TOP").pack(side=TOP)
# b4 = Button(root,text="BOTTOM").pack(side=BOTTOM)

# l1 = Label(root,text="username").grid(row=1,column=1)
# l2 = Label(root,text="email").grid(row=2,column=1)
# l3 = Label(root,text="phone").grid(row=3,column=1)

# t1 = Entry(root).grid(row=1,column=2)
# t2 = Entry(root).grid(row=2,column=2)
# t3 = Entry(root).grid(row=3,column=2)

# b1  =Button(root,text="submit").grid(row=4,column=2)



l1 = Label(root,text="username").place(x=100,y=100)
l2 = Label(root,text="email").place(x=100,y=150)
l3 = Label(root,text="phone").place(x=100,y=200)

t1 = Entry(root)
t1.place(x=200,y=100)
t2 = Entry(root)
t2.place(x=200,y=150)
t3 = Entry(root)
t3.place(x=200,y=200)

b1  =Button(root,text="submit",width=15,command=adduser).place(x=200,y=250)
b2  =Button(root,text="delete",width=15,command=deleteuser).place(x=300,y=250)
b3  =Button(root,text="update",width=15,command=updateuser).place(x=400,y=250)

cols = ("ID","Name","email","phone")
table = ttk.Treeview(root,columns=cols,show="headings")
for col in cols:
    table.heading(col,text=col)
    table.place(x=10,y=300)
show()

table.bind('<Double-Button-1>',getdata)

root.mainloop()