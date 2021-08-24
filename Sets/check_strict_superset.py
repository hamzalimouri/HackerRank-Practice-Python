def check_strict_superset(sets, a_set):
    for s in sets:
        if not a_set.issuperset(s):
            return False
    return True


if __name__ == '__main__':
    a_set = set(input().split())
    n = int(input())

    sets = []
    for _ in range(n):
        sets.append(set(input().split()))

    print(check_strict_superset(sets, a_set))
