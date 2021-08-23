_ = input()
arr = input().split()
a_set = set(input().split())
b_set = set(input().split())

print(sum([(i in a_set) - (i in b_set) for i in arr]))
