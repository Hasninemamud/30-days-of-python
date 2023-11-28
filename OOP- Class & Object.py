class Student:
    roll = ""
    gpa = ""

    def value(self,roll,gpa):
        self.gpa = gpa
        self.roll = roll


    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")

rahim = Student()
rahim.value(101,3.99)
#print(isinstance(rahim,Student))   # object checking
#rahim.roll = 101
#rahim.gpa = 3.67
rahim.display()


kahim = Student()
kahim.value(102,2.99)
#print(isinstance(rahim,Student))   # object checking
#kahim.roll = 101
#kahim.gpa = 3.67
kahim.display()