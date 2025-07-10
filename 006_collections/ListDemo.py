# l = [10,20,30,40,50,20,"Tops",65.23,True]
# l = list((10,20,30))
# print(l)
# print(len(l))
# print(type(l))


#Access list item
# l = ["python","java","php","android","ios"]
# print(l[0])
# print(l[-1])
# print(l[2:])
# print(l[2:4])
# print(l[:5])
# print(l[::-1])


#change item value :
# l = [10,20,30,40,50,60]

# l[2] = 300
# l.insert(2,300)
# l.append(800)

# l[1:3] = []

# l.extend("10")

# j = [100,200,300]
# l.extend(j)

# print(l)


#remove list item
l = [10,20,30,40,50,60]

# l.remove(10)
# l.pop()
# l.pop(1)
# l.clear()
# del l
# print(l)


#loop list / Comprehension
# l = ["A","B","C","D","E"]

# for i in l:
#     print(i)

# for i in range(len(l)):
#     print(l[i])

# i=0
# while i<len(l):
#     print(l[i])
#     i+=1


# l = ["Apple","Banana","Pieapple","Orange","Mango","Grapes"]

# for i in l:
#     if "p" in i:
#         print(i)


# a =  [i for i in l if "p" in i]
# a = [i for i in l if i.startswith("A")]

l = [10,5,65,4,65,48,11,4,3,7,9]

# a = [i for i in l if i%2==0]
# print(a)

# l.sort()
# l.sort(reverse=True)
# l.reverse()
# print(l)

# a = l.copy()
# a = list(l)
# a = l[:]
# print(a)


# x = [10,20,30]
# y = [100,200,300]

# x.extend(y)
# i = x+y
# print(i)

# for i in y:
#     x.append(i)

# print(x)

# print(l.count(4))

# print(l.index(4))