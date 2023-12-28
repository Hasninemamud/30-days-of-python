#Local scope & Global scope

#a = 15 #global scope

def local_a(): #local
    a = 12
    print(a)

    def show_a():
        print(a)

    show_a()
local_a()
