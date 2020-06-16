# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

primes = [2, 3, 5, 7, 11, 13, 17, 19]

num = 1

for i in primes:
    p = i
    while p * i < 20:
        p *= i
    num *= p

print(num)
