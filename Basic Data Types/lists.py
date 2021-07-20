if __name__ == '__main__':
    N = int(input())
    res = []
    for _ in range(N):
        fun, *par = input().split()
        if fun == "print":
            print(res)
        else:
            fun += '(' + ','.join(par)+')'
            eval('res.' + fun)
