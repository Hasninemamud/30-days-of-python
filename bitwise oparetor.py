"""
& = and
| = or
^ = xor
~ = Not(compliment)
<< = left shift
>> = right shift
"""

"""id = [10, 20, 30, 40, 50]
name = ['Hemel', 'Yean', 'Sifat', 'Khan']
result = zip(id, name)

print(list(result))"""
"""
import random
for i in range(1, 9+1):
    n = int(input("Enter a num: "))
    guess_num = random.randint(1,9)
    print(f"guess_num:{guess_num}")
    if n > guess_num:
        print("your guess is almost there")
    else:
        print("Your Guess Is Correct!")"""
import random
for i in range(1, 9):
    i = int(input("Enter a num: "))
    guess_num = random.randint(1,9)
    print(f"guess_num:{guess_num}")
    if i > guess_num:
        print("your guess is almost there")
    else:
        print("Your Guess Is Correct!")