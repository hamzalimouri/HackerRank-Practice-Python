from collections import Counter

_ = input()
sizes = input().split()

counter = Counter(sizes)

res = 0

n = int(input())
for _ in range(n):
    size, price = input().split()
    if counter[size] > 0:
        counter[size] -= 1
        res += int(price)
print(res)
