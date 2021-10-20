import re

n = int(input())
pattern = r"[-|+]?\d*\.\d+"
for _ in range(n):
    nb = input()
    if re.fullmatch(pattern, nb):
        print(True)
    else:
        print(False)
