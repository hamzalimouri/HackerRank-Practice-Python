def merge_the_tools(string, k):
    res = []
    for i in range(0, len(string), k):
        temp = []
        for j in string[i: i + k]:
            if j not in temp:
                temp.append(j)
        res.append(''.join(temp))
    print('\n'.join(res))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)