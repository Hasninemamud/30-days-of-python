class Student:
    roll = ""
    gpa = ""

    def value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa


    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")


rahim = Student()
rahim.value(101,3.50)
rahim.display()

kahim = Student()
kahim.value(102,4.00)
kahim.display()