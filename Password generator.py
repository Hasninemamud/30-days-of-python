import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
          'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "3", "4", "5", "6", "7", "8", "9"]
symbol = ["!", "@", "#", "%", "^", "&", "*", "(", ")"]

print("Welcome to Password Generator ")
n_letters = int(input("Enter how many letters: "))
n_numbers = int(input("Enter how many numbers: "))
n_symbols = int(input("Enter how many symbols: "))

password_list = []

for i in range(1, n_letters ):
    char = random.choice(letter)
    password_list += char
print(password_list)

for i in range(1, n_numbers + 1):
    num = random.choice(numbers)
    password_list += num

for i in range(1, n_symbols + 1):
    sym = random.choice(symbol)
    password_list += sym

# Shuffle the password list to make it more random
random.shuffle(password_list)

# Convert the list to a string
password = ''.join(password_list)

print("Generated Password:", password)
