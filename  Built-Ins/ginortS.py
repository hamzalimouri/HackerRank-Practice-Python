numOdd = []
numeven = []
low = []
upper = []

for c in input():
    if c.isnumeric():
        if int(c) % 2 == 0:
            numeven.append(c)
        else:
            numOdd.append(c)
    elif c.islower():
        low.append(c)
    else:
        upper.append(c)

print(''.join(sorted(low) + sorted(upper) + sorted(numOdd) + sorted(numeven)))
