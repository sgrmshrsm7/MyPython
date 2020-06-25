# Euler discovered the remarkable quadratic formula: n^2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.
# The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
# Considering quadratics of the form: n^2+an+b , where |a|<1000 and |b|≤1000 where |n| is the modulus/absolute value of n e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

def f(n, a, b):
        return (n * n + a * n + b)

primes = []
numbers = [0] * 1000000
p = 2

numbers[0] = 1
numbers[1] = 1

while p < 1000000:
        if numbers[p] == 0:
                primes.append(p)
                i = 2 * p
                while i < 1000000:
                        numbers[i] = 1
                        i += p
        p += 1

max = 0

for a in range(-999, 1000):
        for b in range(-1000, 1001):
                i = 0
                while numbers[f(i, a, b)] == 0:
                        i += 1
                if i > max:
                        max = i
                        maxa = a
                        maxb = b

print(maxa * maxb)