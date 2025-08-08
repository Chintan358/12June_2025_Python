
# print("program started....")

# try :
#     a = 10
#     b  =a/0
# except Exception as e:
#     print(e)
# else:
#     print("Exception not accures")
# finally:
#     print("always executable")

# print("program ended...")



# try: 
#     # a = 10
#     # b  =a/0

#     # a = 10 + "a"
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)



# try:
#     a = "123O"
#     b = int(a)
#     print(b)
# except ValueError as e:
#     print(e)



# try :
#     l = [10,20,30]
#     print(l[5])
# except IndexError as e:
#     print(e)

try : 
    dt = {"a":"Hello"}
    print(dt['b'])
except KeyError as e:
    print(e)

