class A:

    def display(self):
        print("A  : display calling")

class K:
    pass

#single
class B(A):
    pass

#multilevel
# class C(B):
#     pass

#Hierarchical [B&C]
# class C(A):
#     pass

#multiple
class D(A,K):
    pass

# b = B()
# b.display()

# c = C()
# c.display()