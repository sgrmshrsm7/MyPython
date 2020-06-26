# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
# Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
# Pentagonal 	  	Pn=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
# Hexagonal 	  	Hn=n(2n−1) 	  	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
# Find the next triangle number that is also pentagonal and hexagonal.

import math

t = 286
n = 40755
f = 1

while f:
        n += t
        x = (1 + math.sqrt(1 + 24 * n)) / 6
        if x == int(x):
                x = (1 + math.sqrt(1 + 8 * n)) / 4
                if x == int(x):
                        f = 0
        t += 1

print(n)