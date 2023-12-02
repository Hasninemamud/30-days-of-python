nums = 0
sum = 0
for x in range(6):
    x = float(input())
    if x > 0:
        sum = sum + x
        nums = nums + 1

print(f"{nums } valores positivos")
avarg = sum / nums
print(f"{avarg: 0.1f}")