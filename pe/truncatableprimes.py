# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

sum = 0

primes = []
numbers = [0] * 1000000
p = 2

while p < 1000000:
        if numbers[p] == 0:
                primes.append(p)
                i = p
                while i < 1000000:
                        numbers[i] = 1
                        i += p
        p += 1

i = 0

while i < 11:
        for j in primes[8:]:
                j1 = str(j)
                kk = 1
                f = 1
                while kk < len(j1) and f:
                        if int(j1[kk:]) not in primes or int(j1[:kk]) not in primes:
                                f = 0
                        kk += 1
                if f:
                        sum += j
                        i += 1
                        print(sum)
                if i == 11:
                        break

print(sum)