import math

l = [1,5,68,9,4,45,78,95,100]



# a = []
# for i in l:
#     if i%2==0:
#         a.append(i)
# print(a)

# def getEven(num):
#     if num%2==0:
#         return num

# a = filter(getEven,l)
# print(list(a))


# a  =filter(lambda x : x%2==0,l)
# print(list(a))



def check_square(num):
   k = math.sqrt(num)
   if k.is_integer():
      return k


# a = filter(check_square,l)
# print(list(a))


a = filter(lambda x : math.sqrt(x).is_integer() ,l)
print(list(a))