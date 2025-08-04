
# f = open("test.txt",'w')
# f.write("This is my first file io practical")
# f.close()


# f = open("test.txt",'a')
# f.write("Hello Python")
# f.close()

# f = open("test.txt",'r')
# data = f.read()
# print(data)

# f = open("test.txt",'r')
# data = f.readline()
# data1 = f.readline()
# print(data)
# print(data1)


# f = open("test.txt",'r')
# while(True):
#     data = f.readline()
#     if data.startswith('P'):
#         print(data)
#     if not data : 
#         break
# f.close()


# f  = open('test.txt','r')
# data = f.readlines()
# print(data)
# f.close()

        
# with open('test.txt','w') as f : 
#     f.writelines(["Test\n","Tech\n","Python"])

# with open("card-1.jpg",'rb') as f:
#     data = f.read()
#     print(data)

# with open('test.txt','r') as f : 
#     f.seek(5)
#     print(f.tell())
#     data = f.read()
#     print(f.tell())
#     print(data)


# with open("home.txt",'a+') as f:
#     f.write("Hello python, Hello tops")
#     f.seek(0)
#     data = f.read()
#     print(data)


# get data from file if line is conains word 'python'
# count words of each lines



import json

# data = {"name":"Krunal","email":"krunal@gmial.com","Phone":685858585}
l = ["Test","tech","Python"]
with open("mydata.json",'w') as f : 
    json.dump(l,f)


