"""def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
        return sum
print(add(12,33))
"""

n = int(input())
arr = map(int, input().split())

print(sorted(set(arr), reverse=True)[1])

