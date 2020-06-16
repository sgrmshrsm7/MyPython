#   Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#   If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#   For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#   Evaluate the sum of all the amicable numbers under 10000.

array = list(range(1,10000))

sum = 0

for i in range(1,10000):
    c = 0
    for j in range(1,i):
        if i % j == 0:
            c += j
    array[i-1] = c

for i in range(9999):
    if array[i] < 9999:
        if array[array[i] - 1] == i + 1:
            if i + 1 != array[i]:
                sum += i + 1

print(sum)
