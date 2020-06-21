# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
sum = 0

for i in range(10,88777):
        j = str(i)
        s = 0
        for k in j:
                s += factorial[int(k)]
        if s == i:
                sum += i
print(sum)