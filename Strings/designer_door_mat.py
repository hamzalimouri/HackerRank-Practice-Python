if __name__ == '__main__':
    m, n = map(int, input().split())
    pattern = [('.|.' * (2 * i + 1)).center(n, '-') for i in range(m // 2)]
    print('\n'.join(pattern + ['WELCOME'.center(n, '-')] + pattern[::-1]))
