n = int(input("Enter number of rows : "))

print('\nHalf Pyramid')
for i in range(n):
    a = ''
    for j in range(i+1):
        a += str(j + 1)
    print(a)

print('\nInverted Half Pyramid')
for i in range(n):
    a = ''
    for j in range(n-i):
        a += str(j + 1)
    print(a)

print('\nHollow Half Pyramid')
for i in range(n):
    a = ''
    for j in range(i + 1):
        if (i == n - 1) + (j == 0) + (j == i):
            a += str(j + 1)
        else:
            a += ' '
    print(a)

print('\nFull Pyramid')
for i in range(n):
    a = ''
    for j in range(n - i - 1):
        a += ' '
    for j in range(i + 1 , 2 * (i + 1)):
        a += str(j)
    for j in range(2 * i , i , -1):
        a += str(j)
    print(a)

print('\nHollow Full Pyramid')
for i in range(n):
    a = ''
    for j in range(n - i - 1):
        a += ' '
    for j in range(i + 1):
        if (j == 0) + (j == i) + (i == n - 1):
            a += str(j + 1) + ' '
        else:
            a += '  '
    print(a)

print('\nHollow Inverted Half Pyramid')
for i in range(n):
    a = ''
    for j in range(i + 1 , n + 1):
        if (i == 0) + (j == i + 1) + (j == n):
            a += str(j)
        else:
            a += ' '
    print(a)
