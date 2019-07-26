#   The prime factors of 13195 are 5, 7, 13 and 29.
#   What is the largest prime factor of the number 600851475143 ?

a = 600851475143

max = 1

for i in range(2,a):
  if a % i == 0:
    b = 0
    for j in range(2,i):
      if i % j == 0:
        b = b + 1
    if b == 0:
      max = i
      print (max)

print (max)
