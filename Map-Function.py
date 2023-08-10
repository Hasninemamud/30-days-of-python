"""def square(x):
    return x*x
num = [1,2,3,4,5]

result = list(map(square,num))
print(result)"""

#Filter function
def even(x):
    return x%2==0

num = [1,2,3,4,5]
result = list(filter(even,num))
print(result)


