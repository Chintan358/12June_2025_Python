from tkinter import *

root = Tk()
root.geometry("500x500")

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

t1 = Entry(root).place(x=200,y=100)
t2 = Entry(root).place(x=200,y=150)
t3 = Entry(root).place(x=200,y=200)

b1  =Button(root,text="submit",width=17).place(x=200,y=250)


root.mainloop()