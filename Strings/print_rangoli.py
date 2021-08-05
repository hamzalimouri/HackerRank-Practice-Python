import string
alpha = string.ascii_lowercase

def print_rangoli(size):
    res = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        res.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(res[:0:-1]+res))
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)