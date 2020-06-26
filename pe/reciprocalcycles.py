# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given: 1/2 = 0.5, 1/3 = 0.(3), 1/4 = 0.25, 1/5 = 0.2, 1/6	= 0.1(6), 1/7 = 0.(142857), 1/8	= 0.125, 1/9 = 0.(1), 1/10 = 0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

maxv = 0
maxnum = 0

for i in range(2, 1000):
        x = 1
        n = []
        c = 0
        while 1:
                x = x % i
                if x in n:
                        c = len(n) - n.index(x)
                        if c > maxv:
                                maxv = c
                                maxnum = i
                        break
                n.append(x)
                if x == 0:
                        break
                x = x * 10
                
print(maxnum)