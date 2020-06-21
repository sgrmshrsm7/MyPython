# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

a = 1
b = 1

for i in range(11, 100):
        for j in range(i + 1, 100):
                if j % 10 != 0:        
                        i1 = int(i / 10)
                        i2 = i % 10
                        j1 = int(j / 10)
                        j2 = j % 10
                        res = i / j
                        if i1 == j1 and i2 / j2 == res:
                                a *= i2
                                b *= j2
                        elif i1 == j2 and i2 / j1 == res:
                                a *= i2
                                b *= j1
                        elif i2 == j1 and i1 / j2 == res:
                                a *= i1
                                b *= j2
                        elif i2 == j2 and i1 / j1 == res:
                                a *= i1
                                b *= j1

def HCF(a, b):
        if b == 0:
                return a
        else:
                return HCF(b, a % b)

print(int(b / HCF(a, b)))