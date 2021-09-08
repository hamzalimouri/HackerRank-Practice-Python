from itertools import permutations

l, n = input().split()
per = sorted(permutations(l, int (n)))
print('\n'.join(map(lambda a: ''.join(a), per)))