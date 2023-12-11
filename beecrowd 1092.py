n = int(input())

total = 0
c = 0
r = 0
s = 0

for i in range(n):
    i,chr = list(map(str,input().split()))
    i = int(i)
    if (chr == "C"):
        c += i
    elif (chr == "R"):
        r += i
    elif (chr == "S"):
        s += i
total = c+r+s
coelhos = (c*100)/total
Rato = (r*100)/total
Sapo = (s*100)/total
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print(f"Percentual de coelhos: {coelhos:.2f} %")
print(f"Percentual de ratos: {Rato:.2f} %")
print(f"Percentual de sapos: {Sapo:.2f} %")