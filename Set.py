num1 = {1,2,3,4,5}
num2 = set([6,7,8,9])
num2.add(7)
num2.remove(7)

print(num1 )
print( 9 in num2)
print(num1 | num2)
print((num1 & num2))