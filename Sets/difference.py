_, a_set = input(), set(map(int, input().split()))
_, b_set = input(), set(map(int, input().split()))

print(len(a_set.difference(b_set)))
