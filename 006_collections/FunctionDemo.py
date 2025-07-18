
def get_message():
    print("function calling...")

def square(a):
    print(f"square of {a} is {a*a}")

# def add(a,b):
#     # print(f"addition of {a} and {b} is {a+b}")
#     return a+b


# get_message()
# square(5)
# square(10)
# add(10,20)

# a = add(10,20)
# square(a)


# def person(name,email,phone="4554545454",age=0):
#     print(name,email,phone,age)


# person("Hardik","hardik@gmail.com",25)
# person("Hardik","hardik@gmail.com",age=25,phone="415255555")


def add(*a):
    sum =0
    for i in a:
        sum+=i
    print(sum)

# add(10,20,30,40,50,40)


# def person(**a):
#     print(a)


# person(name="abc",email="abc@gmail.com")

# c = lambda a,b : a+b

# print(c(10,20))