if __name__ == '__main__':
    s = input()
    methods = ['isalnum()', 'isalpha()', 'isdigit()', 'islower()', 'isupper()']
    for m in methods:
        print(any([eval('c.' + m)for c in s]))
