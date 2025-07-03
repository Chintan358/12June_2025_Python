
#     *
#    * *
#   * * *
#    * *
#     *

# lines = 7
# stars = 1
# spaces = lines-1
# mid = lines//2
# for i in range(lines):
#     for k in range(spaces):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end="")
#     print()
#     if i<mid:
#         stars+=2
#         spaces-=1
#     else :
#         stars-=2
#         spaces+=1

    #   *
    #  * *
    # *   *
    #  * *
    #   *

# lines = 7
# stars = 1
# spaces = lines-1
# mid = lines//2
# for i in range(lines):
#     for k in range(spaces):
#         print(" ",end="")
#     for j in range(stars):
#         #0 1 2 3 4
#         if j==0 or j==stars-1:
#             print("*",end="")
#         else : 
#             print(" ",end="")
#     print()
#     if i<mid:
#         stars+=2
#         spaces-=1
#     else :
#         stars-=2
#         spaces+=1

# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# 1
# 23
# 456
# 78910

# num=1
# for i in range(5):
#     for j in range(i+1):
#         print(num,end="")
#         num+=1
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

          
# 1  0  1       
# 2  1  12     
# 3  3  23
# 4  6  1234
# 5  10 12345


# 5
# 45
# 345
# 2345
# 12345


# lines = 7
# for i in range(lines,0,-1):
#     for j in range(i,lines+1):
#         print(j,end="")
#     print()

# 0
# 10
# 010
# 1010
# 01010

for i in range(1,6):
    for j in range(1,i+1):
        print(((i+j)%2),end="")
    print()
