#   By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#   What is the 10 001st prime number?

p = 13

i = 6

while i != 10001:
    j = 0
    while j == 0:
        p = p + 1
        c = 0
        for k in range(2,p):
            if p % k == 0:
                c = c + 1
        if c==0:
            j=1
    i = i + 1
    print(p, " ", i)

print (p)
