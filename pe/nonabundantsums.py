# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import math
a = [12]

for i in range(13, 28123 - 11):
    sum = 1
    ul = math.ceil(math.sqrt(i))
    if(ul * ul == i):
        sum += ul
    for j in range(2, ul):
        if i % j == 0:
            sum += j + (i / j)
    if sum > i:
        a.append(i)

sum = 276

for i in range(25, 28124):
    j = 0
    k = len(a) - 1
    f = 0
    while (j <= k) * (f != 1):
        if (a[j] + a[k]) > i:
            k -= 1
        elif (a[j] + a[k]) < i:
            j += 1
        else:
            f = 1
    if f != 1:
        sum += i

print(sum)