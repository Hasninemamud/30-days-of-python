class Student:
    roll = ""
    gpa = ""

rahim = Student()
#print(isinstance(rahim,Student))   # object checking
rahim.roll = 101
rahim.gpa = 3.67
print(f"Roll : {rahim.roll}, GPA : {rahim.gpa}")

kahim = Student()
#print(isinstance(rahim,Student))   # object checking
kahim.roll = 101
kahim.gpa = 3.67
print(f"Roll : {kahim.roll}, GPA : {kahim.gpa}")