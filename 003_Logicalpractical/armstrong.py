number = 153
temp = number
count =0
while number!=0:
    number%10
    number //=10
    count+=1

sum = 0
number = temp
while number!=0:
    rem = number%10
    sum += pow(rem,count)
    number = number//10
if temp == sum:
    print(f"{temp} is armstrong")
else:
    print(f"{temp} is not armstrong")

