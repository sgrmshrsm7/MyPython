num = 1

n = int(input("Enter number of rows : "))

for i in range(n):
    strnum = ''
    for j in range(i + 1):
        strnum += str(num) + ' '
        num += 1
    print(strnum)
