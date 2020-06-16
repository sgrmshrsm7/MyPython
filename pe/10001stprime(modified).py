#   By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#   What is the 10 001st prime number?

primes = [2, 3, 5, 7, 11, 13]

p = 14

while len(primes) != 10001:
    f = 1
    j = 0
    n = len(primes)
    while (j < n) * f:
        if p % primes[j] == 0:
            f = 0
        j += 1
    if f:
        primes.append(p)
    p += 1

print (primes[10000])