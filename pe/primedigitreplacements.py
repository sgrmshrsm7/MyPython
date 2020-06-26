# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

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

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in primes:
        j = str(i)
        n = set()
        for k in j:
                n.add(k)
        for k in n:
                c = 0
                for k1 in nums:
                        if numbers[int(j.replace(k, k1))] == 0 and not (k1 == '0' and k == j[0]):
                                c += 1
                        j = str(i)
                if c == 8:
                        print(i)
                        break
        if c == 8:
                break