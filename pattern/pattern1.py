n = int(input("Enter number of rows : "))

print('\nHalf Pyramid')
for i in range(n):
    a = ''
    for j in range(i+1):
        a += '*'
    print(a)

print('\nInverted Half Pyramid')
for i in range(n):
    a = ''
    for j in range(n-i):
        a += '*'
    print(a)

print('\nHollow Inverted Half Pyramid')
for i in range(n):
    a = ''
    for j in range(n-i):
        if (i == 0) + (j == 0) + (j == n - i - 1):
            a += '*'
        else:
            a += ' '
    print(a)

print('\nFull Pyramid')
for i in range(n):
    a = ''
    for j in range(n - i - 1):
        a += ' '
    for j in range(i + 1):
        a += '* '
    print(a)

print('\nInverted Full Pyramid')
for i in range(n):
    a = ''
    for j in range(i):
        a += ' '
    for j in range(n - i):
        a += '* '
    print(a)

print('\nHollow Full Pyramid')
for i in range(n):
    a = ''
    for j in range(n - i - 1):
        a += ' '
    for j in range(i + 1):
        if (j == 0) + (j == i) + (i == n - 1):
            a += '* '
        else:
            a += '  '
    print(a)
