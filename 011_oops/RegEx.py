import re

# k = re.match("a.b","fdfdfdfacb")
# k = re.search("a.b","fadbdfdfacb")
# k = re.findall("a.b","fadbdfdfacb")

# k = re.match("^Hello","Hello python")
# k = re.search("python","Hello python")

# k = re.search("ab*c","dffdfsabbbbcdfds")
# k = re.search("a+c","dffdfsaaaaacbbbbcdfds")

# k = re.match("^[a-z]{10}$","xccabcdffd")

# k = re.search("^\\+91[\\d]{0,12}$","+91234567898")

# abc@gmail.com

# email = input("enter email : ")
# k = re.search("^[a-zA-Z0-9_-]+@[a-z]+\\.[a-z]{2,4}$",email)

# if k is None:
#     print("Invalid email")
# else : 
#     print("Valid")


st = "abc 7fdsff fdsf 545d  ffds dfsfdf"

k = re.findall("\\d",st)
print(k)