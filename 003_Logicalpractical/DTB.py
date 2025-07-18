
# number = 46
# result = ""
# while number!=0:
#     rem = number%2
#     result = str(rem)+result
#     number=number//2

# print(result)



number = 46
result = 0
mul  = 1
while number!=0:
    rem = number%2  # 0 1 1 1
    result = (rem*mul)+result # 1110 = 
    number=number//2 # 23 11 5 2
    mul=mul*10  # 10000

print(result)




