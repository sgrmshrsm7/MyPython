# There are exactly ten ways of selecting three from five, 12345: 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345.
# In combinatorics, we use the notation, (5C3)=10.
# In general, (nCr)=n!/(r!(n−r)!), where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.
# It is not until n=23, that a value exceeds one-million: (23C10)=1144066.
# How many, not necessarily distinct, values of (nCr) for 1≤n≤100, are greater than one-million?

count = 0

for i in range(1, 101):
        c = 1
        r = 1
        for j in range(i + 1):
                if c > 1000000:
                        count += 1
                c = int((c * (i - r + 1)) / r)
                r += 1

print(count)