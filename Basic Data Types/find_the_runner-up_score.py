if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    set_arr = sorted(list(set(arr)))
    if len(set_arr) == 1:
        print(set_arr[-1])
    else:
        print(set_arr[-2])
