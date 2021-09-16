from collections import namedtuple
n = int(input())
Student = namedtuple('Student', input().split())
marks = [int(st.MARKS) for st in [Student(*input().split()) for _ in range(n)]]
print(round(sum(marks) / n, 2))