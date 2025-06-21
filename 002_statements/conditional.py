
# age = 17
# if age>=18 :
#     print("Elegeble for voting")
# else  : 
#     print("Not elegeble for voting")


a = 100
b = 200
c = 300

# if a>b :
#     if a>c :
#         print("A is greater")
#     else :
#         print("C is greater")
#  :
#     if b>c:
#         print("B is greater")
#     else :
#         print("C is greater")


# if a>b and a>c:
#     print("A is greater")
# elif b>a and b>c:
#     print("B is greater")
# elif c>a and c>b:
#     print("C is greater")
# else:
#     print("No result")


# 91 - 100 : A
# 71 - 90  : B
# 51 - 70  : c
# 36 - 50 : D
# 0 - 35 : F 
# invalid

marks = int(input("enter marks : "))

if marks>90 and marks<=100:
    print("A")
elif marks>70 and marks<=90:
    print("B")
elif marks>50 and marks<=70:
    print("C")
elif marks>35 and marks<=50:
    print("D")
elif marks>=0 and marks<=35:
    print("F")
else:
    print("Invalid marks")