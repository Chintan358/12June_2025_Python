# # a = {"name":"tops","email":"tops@gmail.com"}

# # # print(a['name'])
# # print(a.get('name1'))

# class Test:

#     """
#     Docstring for Test
#     """
#     def disp(self):
#         """
#         Docstring for disp
        
#         :param self: Description
#         """
#         print("Self calling")

# t = Test()
# print(t.disp.__doc__)

# l = [10,20,30]
# k = [20,30,40]

# j = l+k
# print(j)

# from array import array

# k = array('i',[10,20,30,"abc"])
# # print(k)

# keys = ['a','b','c','d','e']
# values = [1,2,3,4,5]  
# d = {}
# for i in range(len(keys)):
#     d.update({keys[i]:values[i]})

# d = {k:v for (k,v) in zip(keys,values)}
# print(d)

# import copy

# k = [[10,20],[30,40]]
# j = copy.copy(k)

# print(j)
# j[0][0] = 100
# print(j)
# print(k)

# j = copy.deepcopy(k)

# print(j)
# j[0][0] = 100
# print(j)
# # print(k)

# l = [4,6,89,4,65,98,5]
# # l.sort()
# # print(l)

# k = sorted(l)
# print(l)
# print(k)

# import logging
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

# logging.debug("This is a debug message")
# logging.error("Error")

# import os
# os.mkdir("Test")
# os.rmdir("Test")
# os.remove("mydata.py")


# import pickle
# # data = {
# #     "name":"Test",
# #     "email":"Test@gmail.com"
# # }

# # with open("test.pkl",'wb') as file : 
# #     pickle.dump(data,file)

# with open("test.pkl",'rb') as file : 
#     data = pickle.load(file)
#     print(data)

# import datetime

# print(datetime.datetime.now())

# choice = 4
# match choice:
#     case 1 :
#         print("Gujarati")
#     case 2 : 
#         print("Hindi")
#     case _:
#         print("Default")