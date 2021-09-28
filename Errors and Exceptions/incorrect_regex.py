import re

n = int(input())
for _ in range(n):
    try:
        reg = re.compile(input())
        print('True')
    except:
        print('False')
