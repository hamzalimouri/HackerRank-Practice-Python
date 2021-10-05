_, n = input().split()

l = []
for _ in range(int(n)):
    l.append(map(float, input().split()))

print('\n'.join(map(lambda x: str(sum(x) / int(n)), zip(*l))))
