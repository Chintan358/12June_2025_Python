
# subjects = {"10":"Python","20":"Java","30":"Node","40":"Php","10":"React"}

# print(subjects)
# print(subjects['10'])
# print(subjects.get("10"))

student = {
    "name":"Krunal",
    "email":"krunal@gmail.com",
    "phone" : "898585968",
    "lang" : ["English","Hindi","Marathi","Gujarati"]
}

# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())


# student['name']="Krunal jadav"
# student['name1']="Krunal jadav"
# student.update({"phone":"123456789","address":"surat"})


# student.pop("name")
# student.popitem()
# student.clear()
# del student
# print(student['lang'][1])

# d = dict(name="Hardik",email="hardik@gmail.com")
# d = {
#     "name":"hardik",
#     "email":"hardik@gmail.com"
# }
# print(d)


# for i in student:
#     print(i)

# for i in student.keys():
#     print(i)

# for i in student.values():
#     print(i)

# for i,j in student.items():
#     print(i)
#     print(j)

users = {
    "u1" : {
        "username":"hardik",
        "password":"hardik123"
    }, 
    "u2" : {
        "username":"harsh",
        "password":"harsh123"
    }, 
    "u3" : {
        "username":"subodh",
        "password":"subodh123"
    }
}

# print(users['u1']['username'])


# for x,y in users.items():
#     for i,j in y.items():
#         print(j)


# u = student.setdefault("name1","test")
# print(u)
# print(student)