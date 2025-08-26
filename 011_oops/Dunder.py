

# class Demo:
#     id = 10
#     name="Hardik"
#     def __init__(self):
#         print("init called")

#     def __str__(self):
#         return f"my id is {self.id} and name is {self.name}"


# d = Demo()
# print(d)


# class Calc:

#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c

#     # def __add__(self,obj):
#     #     return self.a+obj.a,self.b+obj.b,self.c+obj.c

#     def __mul__(self,obj):
#         return self.a*obj.a,self.b*obj.b,self.c*obj.c
 
# c1 = Calc(10,20,40)
# c2 = Calc(30,40,80)


# k = c1*c2
# print(k)


# class Demo:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def __eq__(self, value):
#         return self.a==value.a and self.b==value.b


# d1 = Demo(10,20)
# d2 = Demo(10,20)

# print(d1==d2)


class Sample:
    def __init__(self,a):
        self.a  =a

    # def __len__(self):
    #     return len(self.a)
    
    # def __str__(self):
    #     return str(len(self.a))

    def __setitem__(self,i,v):
        self.a[i] = v
        print(self.a)

    def __getitem__(self,i):
        return  self.a[i]

s = Sample([10,20,30,40])
# print(len(s))
# print(s)

# s[2] = 5000
# print(s[2])

del s
print(s)
