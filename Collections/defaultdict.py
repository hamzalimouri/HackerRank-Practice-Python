from collections import defaultdict

d = defaultdict(list)
l = []
n, m = map(int, input().split())

for i in range(n):
    d[input()].append(str(i + 1))
    
for i in range(m):
    l.append(input())
    
for i in l:
    print(' '.join(d[i]) if i in d else -1)