row = int(input("Enter number of rows : "))

col = int(input("Enter number of columns : "))

print('\nSolid Rectangle')
for i in range(row):
    a = ''
    for j in range(col):
        a += '*'
    print(a)

print('\nHollow Rectangle')
for i in range(row):
    a = ''
    for j in range(col):
        if (i == 0) + (j == 0) + (i == row - 1) + (j == col - 1):
            a += '*'
        else:
            a += ' '
    print(a)
