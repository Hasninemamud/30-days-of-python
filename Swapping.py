"""a = int(input("Enter the 1st value: ")) # 12
b = int(input("Enter the 2nd value: ")) # 43

a,b = b,a
print("A : ",a)
print("B : ",b)
"""
n = int(input())

for i in range(n):
    X, H = input().split()

    if X >= H:
        print("Yes")
    else:
        print("No")