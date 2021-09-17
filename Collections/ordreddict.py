from collections import OrderedDict

n = int(input())
items = OrderedDict()
for _ in range(n):
    fields = input().split()
    name = " ".join(fields[:-1])
    items[name] = items.get(name, 0) + int(fields[-1])
    
print('\n'.join(map(lambda name: f'{name} {items[name]}', items)))