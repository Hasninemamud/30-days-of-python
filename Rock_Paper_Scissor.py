import random
print("Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors")
user_choice = int(input("Enter your choice:  "))
if user_choice >=3 or user_choice < 0:
    print("you Enter a Invalid  Number & You Lose")
else:
    computer_choice = random.randint(0,2)
    print(f"Computer choice: {computer_choice}")

    if computer_choice == user_choice:
         print("Draw")
    elif user_choice == 0 and computer_choice == 2:
         print("You Win")
    elif user_choice == 2 and computer_choice == 0:
         print("You Lose")
    elif user_choice > computer_choice:
         print("You Win")
    elif user_choice < computer_choice:
         print("You Lose")





