# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

primes = []
numbers = [0] * 1000000
p = 2

while p < 1000000:
        if numbers[p] == 0:
                primes.append(p)
                i = 2 * p
                while i < 1000000:
                        numbers[i] = 1
                        i += p
        p += 1

cprimes = []

for i in primes:
        j = str(i)
        k = 0
        f = 1
        while k < len(j) and f:
                if numbers[int(j)]:
                        f = 0
                j = j[1:] + j[0]
                k += 1
        if f:
                cprimes.append(i)

print(len(cprimes))