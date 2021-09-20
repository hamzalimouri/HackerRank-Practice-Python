from collections import deque

n = int(input())
d = deque()
for _ in range(n):
    func, *attr = input().split()
    getattr(d, func)(*attr)
print(' '.join(d))
