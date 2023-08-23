import re
pattern = r"^colo.r$"

if re.match(pattern,"coloar"):
    print("Match")

else:
    print("Not Match")
