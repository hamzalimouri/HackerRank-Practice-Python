def minion_game(string):
    v = 'AEIOU'
    k = s = 0
    l = len(string)
    for i in range(l):
        if string[i] in v:
            k += l - i
        else:
            s += l - i
    if k > s:
        print(f'Kevin {k}')
    elif k < s:
        print(f'Stuart {s}')
    else:
        print('Draw')
    
if __name__ == '__main__':
    s = input()
    minion_game(s)