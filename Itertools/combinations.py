from itertools import combinations

l, n = input().split()
l = sorted(l)

for i in range(1, int(n) + 1):
    com = sorted(combinations(l, i))
    print('\n'.join(map(lambda a: ''.join(a), com)))
