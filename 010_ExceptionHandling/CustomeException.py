
class MyException(Exception):
    def __init__(self,message):
        super().__init__(message)

class Demo:
    def ageCheck(self,age):
        if age<18:
            raise MyException("Invalid age.")

d = Demo()
d.ageCheck(15)

