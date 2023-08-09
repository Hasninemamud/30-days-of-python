"""n = input("Enter the number: ")
list = n.split()
sum = 0

for num in list:
    sum = sum + int(num)
print(sum)"""

numOfWord = 0
numOfLetters = 0
numOfDigit =0

text = input("Enter the text: ")
for x in text:
    if x >= "a" and x <= "z" :
        numOfLetters = numOfLetters + 1
    #x = x.lower()
    elif x >= "A" and x <= "Z":
        numOfLetters = numOfLetters + 1
    elif x >= "0" and x <= "9":
        numOfDigit = numOfDigit + 1
    elif x == " ":
        numOfWord = numOfWord + 1

print("Number of Letters: ", numOfLetters)
print("Number of Digit: ", numOfDigit)
print("Number of Word: ", numOfWord+1)

