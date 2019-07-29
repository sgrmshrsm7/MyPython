#   You are given the following information, but you may prefer to do some research for yourself.
#       1 Jan 1900 was a Monday.
#       Thirty days has September,
#       April, June and November.
#       All the rest have thirty-one,
#       Saving February alone,
#       Which has twenty-eight, rain or shine.
#       And on leap years, twenty-nine.
#       A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#   How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

count = 0

c = 1

for i in range(1901 , 2001):
    for j in range(1 , 13):
        if j < 8:
            if j != 2:
                if j % 2 == 0:
                    d = 30
                else:
                    d = 31
            else:
                if (i % 4 == 0) * (i % 400 != 0):
                    d = 29
                else:
                    d = 28
        else:
            if j % 2 == 0:
                d = 31
            else:
                d = 31
        if c == 0:
            count += 1
        for k in range(d):
            c += 1
            if c == 7:
                c = 0

print(count)
