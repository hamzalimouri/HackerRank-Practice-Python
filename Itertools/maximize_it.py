from itertools import product
from collections import defaultdict

d = defaultdict(list)

n, m = map(int, input().split())

for i in range(n):
    d[i].extend(map(lambda x: int(x) ** 2, input().split()[1:]))

res = 0
    
for p in product(*d.values()):
    res = max(res, sum(p) % m)

print(res)