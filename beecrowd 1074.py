n = int(input())
for i in range(n):
    i = int(input())
    if i < 0:
        if i % 2 == 0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")

    if i > 0:
        if i % 2 == 0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")

    elif i == 0:
        print("NULL")
