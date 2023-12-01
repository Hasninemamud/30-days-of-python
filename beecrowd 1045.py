
A,B,C = map(float,input().split())

if (A >= B + C):
    print("NAO FORMA TRIANGULO")
elif(A*A == B*B + C*C):
    print("TRIANGULO RETANGULO")
if(A*A > B*B + C*C):
    print("TRIANGULO OBTUSANGULO")
elif (A * A < B * B + C * C):
    print("TRIANGULO ACUTANGULO")

if(A == B == C):
    print("TRIANGULO EQUILATERO")
elif(A == B or B == C or A == C):
    print("TRIANGULO ISOSCELES")



