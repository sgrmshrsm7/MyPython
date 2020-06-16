#   The prime factors of 13195 are 5, 7, 13 and 29.
#   What is the largest prime factor of the number 600851475143 ?

a = 600851475143

max = 1

p = 3

while a != 1:
    while a % p == 0:
      a = a / p
      max = p
    p += 1

print (max)