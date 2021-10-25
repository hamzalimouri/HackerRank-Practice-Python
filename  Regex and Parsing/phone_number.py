import re

pattern = re.compile(r'[789]\d{9}$')

n = int(input())
for _ in range(n):
    num = input()
    if pattern.match(num):
        print('YES')
    else:
        print('NO')
