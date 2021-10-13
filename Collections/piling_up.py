def to_virtical(row):
    l = len(row)
    v = row[0] if row[0] >= row[-1] else row[-1]
    for i in range(l // 2):
        if v >= row[i] >= row[-1 - i]:
            v = row[i]
        elif v >= row[-1 - i] >= row[i]:
            v = row[-1 - i]
        else:
            return False
    if l % 2 and v < row[i + 1]:
        return False
    return True

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        _ = input()
        row = list(map(int, input().split()))
        print('Yes' if to_virtical(row) else 'No')