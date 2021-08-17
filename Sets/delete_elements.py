n = int(input())
s = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    f, *kw = input().split()
    if kw:
        getattr(s, f)(*map(int, kw))
    else:
        getattr(s, f)()
print(sum(s))