
c = 0
d = 0
while(True):
    try:
        if d == 2:
           break
        a = float(input())
        if a >= 0 and a <= 10:
            d += 1
            c += a
        else:
            print("nota invalida")
    except EOFError:
        break
b = c/2
print(f'media = {b}')
