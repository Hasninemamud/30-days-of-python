a,b,c = map(str,input().split())
if (a == "vertebrado"):
    if b == "ave":
        if c == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    elif b == "mamifero":
        if c == "onivoro":
            print("homem")
        else:
            print("vaca")
if (a == "invertebrado"):
    if b == "inseto":
        if c == "hematofoga":
            print("pulga")
        else:
            print("lagarta")
    elif b == "anelideo":
        if c == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")


