#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

i=1
num = 2520
while i!=0:
    num = num + 1
    count = 0
    for j in range(1,21):
        if num % j == 0:
            count = count + 1
    if count == 20:
        i=0

print (num)
