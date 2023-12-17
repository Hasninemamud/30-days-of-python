def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def divi(x,y):
    return x / y
def moduls(x,y):
    return  x % y

print("Select Option:")
print("1. add")
print("2. sub")
print("3. mul")
print("4. div")
print("5. modulas")

while(True):
    take = input("(Choice 1/2/3/4/5): ")
    if take in ("1","2","3","4","5"):
        try:
            x = float(input("Enter 1st number: "))
            y = float(input("Enter 2nd number: "))
        except ValueError:
            print("Invalid input, Please take a Number input")
            continue
        if take == "1":
            print(f"X + Y ={x+y}")
        elif take == "2":
            print(f"X - Y ={x-y}")
        elif take == "3":
            print(f"X * Y ={x*y}")
        elif take == "4":
            print(f"X / Y ={x/y}")
        elif take == "5":
            print(f"X % Y ={x%y}")

        exit = input("Continue calculation (Yes/No): ")
        if exit == "No":
            break
        else:
            continue





