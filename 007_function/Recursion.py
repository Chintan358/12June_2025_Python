

# def test():
#     print("calling")
#     test()
# test()


def square(num):
    print(f"square of {num} is {num*num}")
    num+=1
    if num<=100:
        square(num)


square(5)