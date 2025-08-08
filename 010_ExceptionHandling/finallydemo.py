

# def  test():
#     try : 
#         a = int(input("enter number : "))
#         return a
#     except ValueError as e:
#         return e
#     finally :
#         print("always exceutable...")
    

# k = test()
# print(k)



try :  
    f = open("test1.txt",'r')
    # f.write("Hello")
    k = f.read()
    print(k)
  
except Exception as e:
    print(e)
finally : 
     try :
        f.close()
     except Exception as e :
         print(e)