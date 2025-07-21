from functools import reduce

l = [10,20,30,40,50,450]

# sum =0
# for i in l:
#     sum+=i
# print(sum)

# def sum(x=0,y=0):
#     print(x,y)
#     x = x+y
#     return x

# a = reduce(sum,l)
# print(a)

# a = reduce(lambda x,y: x+y,l)
# print(a)

# def max(x,y):
#     if x>y:
#         return x
#     else:
#         return y

# a  =reduce(lambda x,y : x if x>y else y,l)
# print(a)