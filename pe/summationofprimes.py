#   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#   Find the sum of all the primes below two million.

sum = 0

prime = [2, 3, 5]

for i in range (6,2000000):
    c = 0
    for j in prime:
        if i % j == 0:
            c = 1
            break
    if c == 0:
        prime.append(i)

for i in prime:
    sum = sum + i

print (sum)
