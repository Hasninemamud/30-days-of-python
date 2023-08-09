
from collections import deque

bank = deque(["Hemel","Hasninen","Yean"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()

if not bank:
    print("No person left here")
