_, a_set = input(), set(map(int, input().split()))
n = int(input())
for _ in range(n):
    f, _ = input().split()
    new_set = set(map(int, input().split()))
    eval(f'a_set.{f}(new_set)')
print(sum(a_set))
