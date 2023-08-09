import random
guess_number = int(input("Enter the number from 1 to 100: "))
randomNumber = random.randint(1,100)

if guess_number == randomNumber:
    print("You Win")
else:
    print("You Lose")
    print( "Random Number is: ",randomNumber)