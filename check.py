def name():
    what = input("What is your name: ")
    print(f"Hello {what}")

def age():
    num = int(input("Enter the age: "))
    if num < 13:
        print("Not Allowed")
    else:
        print("Allowed")
