from itertools import combinations_with_replacement
s, n = input().split()
com = combinations_with_replacement(sorted(s), int(n))
print('\n'.join(map(lambda a: ''.join(a), com)))