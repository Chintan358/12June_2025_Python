

# l = [10,20,30,40,50,60]
# def square(num):
#     return num*num

# a = []
# for i in l:
#     j =  square(i)
#     a.append(j)
# print(a)


# a = map(square,l)
# print(list(a))

# a = map(lambda num:num*num,l)
# print(list(a))



a = [10,20,30,40,50,60]
b = [1,2,3,4,5,6]

c = map(lambda x,y : x*y,a,b)
print(list(c))




