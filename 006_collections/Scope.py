

a = 10
def test():
    global a
    a = 20
    print(a)

def demo():
    global a
    a = 40
    print(a)

test()
demo()
print(a)




