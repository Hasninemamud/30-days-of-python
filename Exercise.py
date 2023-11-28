class Triangle:
    height = " "
    base = " "

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        area = .5 * self.base * self.height
        print("Area = ",area)

t1 = Triangle(10,20)
t1.calculate_area()