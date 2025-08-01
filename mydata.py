from user import details
from user.details import *

# details.msg()
# msg()


# l = [10,20,5,6,49,89,4,0,4]

# l.sort()
# print(l)

# k = sorted(l)
# print(k)


# subject = ["Java","Python","Node",'Php',"Android"]
# code = ["J","Py","N","Ph"]
# scode = {}

# for i in range(len(code)):
#     scode.update({subject[i]:code[i]})
# print(scode)


# l = [10,20,30,40,{"name":"krunal","email":"krunal@gmail.com"}]

# print(l[4]['name'])


s = "sun rises in east"

count = {}

for i in s:
    if count.get(i) is None:
        count.update({i:1})
    else:
        k = count.get(i)
        k+=1
        count.update({i:k})


print(count)