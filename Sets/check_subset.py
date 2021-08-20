n = int(input())
for _ in range(n):
    _, a_set = input(), set(input().split())
    _, b_set = input(), set(input().split())
    a_set.difference_update(b_set)
    if a_set:
        print(False)
    else:
        print(True)
