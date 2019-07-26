#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def rev(a):
    n=0
    b=a
    while b != 0:
        n = n*10 + b%10
        b = (b - b%10) / 10
    return n

def palin(a):
    if rev(a) == a:
        return 1
    else:
        return 0

largest_palin = 0

for i in range(900,1000):
    for j in range(900,1000):
        if palin(i*j) == 1 and i*j > largest_palin:
            largest_palin = i*j

print (largest_palin)
