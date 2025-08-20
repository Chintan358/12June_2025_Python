

class Demo:
    id = 10
    name="Hardik"
    def __init__(self):
        print("init called")

    def __str__(self):
        return f"my id is {self.id} and name is {self.name}"


d = Demo()
print(d)