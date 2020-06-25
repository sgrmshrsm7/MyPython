# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?

numbers = [0] * 10000
p = 2

while p < 10000:
        if numbers[p] == 0:
                i = 2 * p
                while i < 10000:
                        numbers[i] = 1
                        i += p
        p += 1

def perm(i, j):
        a = str(i)
        b = str(j)
        ad = {}
        bd = {}
        for i in a:
                if i in ad:
                        ad[i] += 1
                else:
                        ad[i] = 1
        for i in b:
                if i in bd:
                        bd[i] += 1
                else:
                        bd[i] = 1
        if ad == bd:
                return True
        else:
                return False

for i in range(1000, 10000):
        if i != 1487 and numbers[i] == 0:
                for d in range(1, (10000 - i) // 2):
                        if numbers[i + d] == 0 and numbers[i + 2 * d] == 0:
                                if perm(i, i + d) and perm(i, i + 2 * d):
                                        print(str(i) + str(i + d) + str(i + 2 * d))
