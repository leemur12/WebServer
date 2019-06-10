class Parent:
    def __init__(self, x, y):
        self.x= x
        self.y= y
        self.r= RandO(1, 2)
        self.cool()

class Child(Parent):
    def __init__(self, x, y, z):
        Parent.__init__(self, x, y)
        self.y= y

    def cool(self):
        self.x= 20


class RandO:
    def __init__(self, a, b):
        self.a= a
        self.b= b

s= Child(3,4,5)

print(s.x)
s.x=40
print(s.x)
