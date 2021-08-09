_ = input()
m = set(map(int, input().split()))
_ = input()
n = set(map(int, input().split()))

a = m.difference(n)
b = n.difference(m)

print('\n'.join(map(str, sorted(a.union(b)))))
