from collections import Counter
_, l = input(), input().split()

counter = Counter(l)
print(counter.most_common()[-1][0])
