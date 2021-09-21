from itertools import combinations

_ = input()
k = input().split()
n = int(input())

coms = list(combinations(k, n))

print(sum(['a' in com for com in coms]) / len(coms))
