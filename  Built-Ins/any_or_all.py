_ = input()
nbs = input().split()
print(all(int(n) > 0 for n in nbs) and any(n == n[::-1] for n in nbs))
