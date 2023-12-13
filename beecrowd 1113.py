while(True):
    a,b = list(map(int,input().split()))
    if a<b:
        print("Crescente")
    elif a>b:
       print("Decrescente")
    if a == b:
        break

