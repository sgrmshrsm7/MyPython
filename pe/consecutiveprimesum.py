# The prime 41, can be written as the sum of six consecutive primes: 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

max = 953
d = 21
sum = 0

for d in range(21, 1000):
        sum = 0
        for i in range(d):
                sum += primes[i]
        i = d
        while sum < 1000000:
                if numbers[sum] == 0:
                        max = sum
                sum -= primes[i - d]
                sum += primes[i]
                i += 1

print(max)