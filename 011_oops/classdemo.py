
# class Demo :
#     a = 20
#     b = 20

#     def test(self):
#         print(self.a,self.b)
    
#     def sample(self):
#         print("sample calling...")

# d1 = Demo()
# d1.test()
# d1.sample()


# class Student:
   
#     def display(self):
#         print(self.id,self.name)


# s1 = Student()
# s1.id=20
# s1.name="Krunal"
# s1.display()


# s2 = Student()
# s2.id=10
# s2.name="hardik"
# s2.display()

# s3 = Student()
# s3.display()



#********constructor***********



# class Emp:

#     def __init__(self,id,name,email):
#         self.id = id
#         self.name=name
#         self.email = email
        


#     def display(self):
#         print(self.id,self.name,self.email)

#     def test(self):
#         print(self.id)


# e1 = Emp(10,"krunal","krunal@gmial.com")
# e1.display()
# e1.test()

# e2 = Emp(20,"harsh","harsh@gmail.com")
# e2.display()

# e3 = Emp()




# class Emp:

#     def __init__(self,id,name,email):
#         print(id,name,email)


# e1 = Emp(10,"krunal","krunal@gmial.com")


# e2 = Emp(20,"harsh","harsh@gmail.com")




# class Emp:

#     def __init__(self,*a,):
#         sum = 0
#         for i in a:
#             sum += i
#         print(sum)

    


# e1 = Emp(10,20)
# e2 = Emp(10,20,30)
# e3 = Emp(10,20,30,40,50,60)




class Test:

    clg = 'DRSTC'

    def __init__(self,id,name):
        self.id = id
        self.name = name
    
    def disp(self):
        print(self.id,self.name,self.clg)
    

    def display(self):
        self.id = 45
        self.clg= "abc"
        print(self.id,self.clg)

    @classmethod
    def run(cls):
        cls.id = 50
        cls.clg= "abc"
        print(cls.id,cls.clg)

    # @staticmethod
    # def sample():
    #     print("Hello...sample calling")


# t1 = Test()
# t1.display()

# Test.run()
# Test.sample()

# t4 = Test(10,"krunal")
# Test.clg="Tapi clg"
# t4.disp()


# t5 = Test(20,"Subodh")
# t5.disp()

t5 = Test(20,"xyz")
t5.display()

Test.run()