# The first two consecutive numbers to have two distinct prime factors are: 14 = 2 × 7, 15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are: 644 = 2² × 7 × 23, 645 = 3 × 5 × 43, 646 = 2 × 17 × 19.
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

primes = []
numbers = [0] * 1000000
p = 2

while p < 1000000:
        if numbers[p] == 0:
                primes.append(p)
                i = p
                while i < 1000000:
                        numbers[i] += 1
                        i += p
        p += 1
        
for i in range(len(numbers) - 3):
        if numbers[i] == 4 and numbers[i + 1] == 4 and numbers[i + 2] == 4 and numbers[i + 3] == 4:
                print(i)
                break