n = float(input())
if(n >= 0 and n <= 2000):
    print("Isento")
elif(n >= 2000.01 and n <= 3000):
    n = n - 2000
    x = n * .08
    print("R$ %.2f" %x)
elif(n >= 3000.01 and n <= 4500):
    n = n - 3000
    x = n * .18+80
    print("R$ %.2f" %x)
else:
   n = n - 4500
   x = n * .28+350
   print("R$ %.2f"%x)