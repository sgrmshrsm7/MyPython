#   If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#   If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#   NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

numbers = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight' , 'nine']

numbers1 = ['ten' , 'eleven' , 'twelve' , 'thirteen' , 'fourteen' , 'fifteen' , 'sixteen' , 'seventeen' , 'eighteen' , 'nineteen']

numbers2 = ['twenty' , 'thirty' , 'forty' , 'fifty' , 'sixty' , 'seventy' , 'eighty' , 'ninety']

last = 'onethousand'

sum = len(last)

for i in range(1,1000):
    a = i / 100
    b = i / 10
    c = i % 10
    if a > 0:
        sum += len(numbers[a-1] + 'hundred')
        if i % 100 > 0:
            sum += len('and')
    if b % 10 == 1:
        sum += len(numbers1[i % 10])
    elif b % 10 == 0:
        if i % 10 > 0:
            sum += len(numbers[c-1])
    else:
        sum += len(numbers2[(b % 10) - 2])
        if i % 10 > 0:
            sum += len(numbers[c-1])

print(sum)
