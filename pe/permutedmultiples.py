# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

f = True
i = 100000

while f:
        j = str(i)
        if j[0] == '1':
                n1 = {}
                for k in j:
                        if k not in n1:
                                n1[k] = 1
                        else:
                                n1[k] += 1
                k = 2 * i
                for k1 in range(5):
                        k2 = str(k)
                        n2 = {}
                        for k3 in k2:
                                if k3 not in n2:
                                        n2[k3] = 1
                                else:
                                        n2[k3] += 1
                        if n1 != n2:
                                done = 0
                                break
                        else:
                                done = 1
                        k += i
                if done == 1:
                        print(i)
                        f = False
        i += 1