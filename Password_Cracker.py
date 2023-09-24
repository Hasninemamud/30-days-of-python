import os
from random import *

u_pwd = input("Enter your Password: ")
possible_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'u', 'v', 'w', 'x', 'y', 'z',
                      '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

guess_pwd = ""
while guess_pwd != u_pwd:
    guess_pwd = ""
    for _ in range(len(u_pwd)):
        guess_pwd += possible_characters[randint(0, len(possible_characters) - 1)]
    print(guess_pwd)
    print("Cracking Password.........Please wait")
    os.system("cls")

print("Your Password Is: ", guess_pwd)
