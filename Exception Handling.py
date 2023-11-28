"""try:
    list = [20,0,30]
    result = list[0] / list[3]
    print(result)
    print("Done")
except (ZeroDivisionError,IndexError):
    print("Dividing by zero is not possible")
finally:
    print("Successful")
"""

try:
    result = 20 / 0
    print(result)

except ZeroDivisionError:
    print("division by zero not possible")

