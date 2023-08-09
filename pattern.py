"""n = int (input("Enter the number : "))
for i in range(n+1):
    print( i *  "*")"""


"""n = int (input("Enter the number : "))
for i in range(1,n+1,2):
    print( i *  "*")"""

n = int (input("Enter the number : "))
for i in range(n+1):
   print(" " * (n - i) + "*" * i)