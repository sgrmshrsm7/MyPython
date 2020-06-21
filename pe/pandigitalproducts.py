# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

prod = set()

for i in range(2, 10):
        for j in range(1234, 9877):
                n = set()
                n.add(i)
                j1 = str(j)
                if '0' not in j1:
                        for k in j1:
                                n.add(int(k))
                        if len(n) == 5:
                                k1 = str(i * j)
                                if '0' not in k1 and len(k1) == 4:
                                        for k in k1:
                                                n.add(int(k))
                                        if len(n) == 9:
                                                prod.add(i * j)
                                                # print(str(i) + '*' + str(j) + '=' + k1)

for i in range(12, 99):
        if i % 11 != 0 and i % 10 != 0:
                for j in range(123, 988):
                        n = set()
                        n.add(i % 10)
                        n.add(int(i / 10))
                        j1 = str(j)
                        if '0' not in j1:
                                for k in j1:
                                        n.add(int(k))
                                if len(n) == 5:
                                        k1 = str(i * j)
                                        if '0' not in k1 and len(k1) == 4:
                                                for k in k1:
                                                        n.add(int(k))
                                                if len(n) == 9:
                                                        prod.add(i * j)
                                                        # print(str(i) + '*' + str(j) + '=' + k1)

sum = 0
for i in prod:
        sum += i
print(sum)