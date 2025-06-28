# 0 1 1 2 3 5 8 13 21 34 55 89 144  233

a = 0  #1 1 2
b = 1  #1 2 3
print(a, b, end=" ")

for i in range(1,100):
    c = a+b #1 2 3 5
    a = b
    b = c
    print(c,end=" ")