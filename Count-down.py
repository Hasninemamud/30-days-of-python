# import time
# num = int(input("Enter the number: "))
# while num >= 0:
#     print(num)
#     num = num - 1
#     time.sleep(1)
#
#
word = "hasnine_203002004_CSE425.pdf"
# index_of_us = word.index("_")
# print(index_of_us)
# roll = word[index_of_us + 1:index_of_us + 10]
# print(roll)

div = word.split("_")

name = div[0]
roll = div[1]
course = div[2]
print(f"Name:{name},Roll: {roll}, Course: {course}")