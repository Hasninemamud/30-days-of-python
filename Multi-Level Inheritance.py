class A:
    def display1(self):
        print("I am in A class")

class B(A):
    def display2(self):
        print("I am in B class")

class C(B):
    def display3(self):
        print("I am in C class")

result = C()
result.display1()
result.display2()
result.display3()