class shape:
    area = 0
    def area(self):

        print("area of square is: ",area)

class square(shape):
    def __init__(self,length):
        self.length=length

    def area(self):
        area=self.length**2
        print("area of square is: ",area)

y=shape()
y.area()
x=square(7)
x.area()
