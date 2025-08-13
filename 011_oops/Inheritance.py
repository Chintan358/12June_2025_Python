
class Animal:
    
    
    def __init__(self):
        print("animal class calling...")
    
    def voice(self):
        print("animal voice....")


class Dog(Animal):
    
    def voice(self):
        print("wow..wow")

class Cat(Animal):
    
    def voice(self):
        print("meow..meow")


d  = Dog()
c = Cat()

d.voice()
c.voice()