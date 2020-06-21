# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

def DtB(n):
        return bin(n).replace("0b", "")

sum = 0

for i in range(1000000):
        j = str(i)
        if j == j[::-1]:
                j = str(DtB(int(j)))
                if j == j[::-1]:
                        sum += i

print(sum)