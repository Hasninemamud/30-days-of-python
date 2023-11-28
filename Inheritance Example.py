# Hierarchical Inheritance
class shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

class Triangle(shape):
    def Triangle(self):
        Triangle= 0.5 * self.dim1 * self.dim2
        print("Area of Triangle:  ",Triangle)


class Rectangle(shape):
    def Rectangle(self):
        Rectangle = self.dim1 * self.dim2
        print("Area of Rectangle:  ", Rectangle)


result = Triangle(20,30)
result.Triangle()

r1 = Rectangle(20,30)
r1.Rectangle()
