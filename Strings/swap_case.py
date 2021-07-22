def swap_case(s):
    res = []
    for c in s:
        if c.islower():
            res.append(c.upper())
        else:
            res.append(c.lower())
    return ''.join(res)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)