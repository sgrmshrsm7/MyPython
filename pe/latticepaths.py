#   Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#   How many such routes are there through a 20×20 grid?

def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f

def C(n,r):
    return fact(n)/(fact(n-r)*fact(r))

n = 20

r = 21

print(C(n + r - 1,r - 1))
