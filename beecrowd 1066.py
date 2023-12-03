"""even=0
odd=0
positive=0
negative=0
for i in range(5):
    n = float(input())
    if(n % 2 == 0):
         even = even+1
    else:
        odd =odd+1
    if (n > 0):
        positive =positive+1
    elif (n < 0):
        negative =negative+1
print(f"{even} valor(es) par(es)")
print(f"{odd} valor(es) impar(es)")
print(f"{positive} valor(es) positivo(s)")
print(f"{negative} valor(es) negativo(s)")"""
even = 0
odd = 0
positive = 0
negative = 0

for i in range(5):
    i = float(input())
    if i>0:
        positive += 1
    elif(i<0):
        negative += 1
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"{even}valor(es) par(es)")
print(f"{odd}valor(es) impar(es)")
print(f"{positive}valor(es) positivo(s)")
print(f"{negative}valor(es) negativo(s)")
