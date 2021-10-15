def cube(x): return x ** 3


def fibonacci(n):
    res = [0, 1]
    for i in range(n - 2):
        res.append(res[-1] + res[-2])
    return res[0:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
