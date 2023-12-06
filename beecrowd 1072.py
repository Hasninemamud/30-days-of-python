x = int(input())
inn = 0
out = 0
for i in range(x):
    i = int(input())
    if 10<=i<=20:
        inn += 1
    else:
        out += 1
print(f"{inn} in")
print(f"{out} out")