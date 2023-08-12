def voter(age):

    if age < 18:
        raise ValueError("Invalid Voter")
    return "You are Eligible"

age = int(input("Enter your age: "))

try:
    print(voter(age))

except ValueError as error:
    print(error)