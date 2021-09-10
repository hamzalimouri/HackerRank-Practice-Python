from itertools import groupby

l = input()

for k, g in groupby(l):
    print(f'({len(list(g))}, {k})', end=' ')
