number = 121
temp = number
sum = 0
while number!=0:
    rem = number%10
    sum = sum*10 + rem
    number //=10

if temp==sum:
    print("pelindrom")
else : 
    print("Not pelindrom")

