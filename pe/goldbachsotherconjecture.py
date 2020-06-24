# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import math

primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

n = 37
f = 1

while f:
        c = 0
        for i in primes:
                if n % i == 0:
                        c = 1
                        break
        if c:
                for i in primes:
                        x = math.sqrt((n - i) / 2)
                        if x == int(x):
                                c = 0
                if c:
                        print(n)
                        f = 0
        else:
                primes.append(n)
        n += 2