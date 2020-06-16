#   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#   Find the sum of all the primes below two million.

numbers = [0] * 2000000
p = 2
sum = 0

while p < 2000000:
    if numbers[p] == 0:
        sum += p
        i = p
        while i < 2000000:
            numbers[i] = 1
            i += p
    p += 1

print(sum)