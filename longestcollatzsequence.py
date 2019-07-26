#   The following iterative sequence is defined for the set of positive integers:
#   n => n/2 (n is even)
#   n => 3n + 1 (n is odd)
#   Using the rule above and starting with 13, we generate the following sequence:
#   13 => 40 => 20 => 10 => 5 => 16 => 8 => 4 => 2 => 1
#   It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#   Which starting number, under one million, produces the longest chain?
#   NOTE: Once the chain starts the terms are allowed to go above one million.

max = 10

maxnum = 13

for i in range(14,1000000):
    s = i
    n = 1
    while s > 1:
        if s % 2 == 0:
            s = s / 2
        else:
            s = 3 * s + 1
        n = n + 1
    if n > max:
        max = n
        maxnum = i
    print(i)
print(maxnum)
