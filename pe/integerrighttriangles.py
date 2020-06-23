# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?

max = 3
maxp = 120

for i in range(31, 1001):
        n = []
        for j in range(1, int(i / 3)):
                for k in range(j, int(2 * i / 3)):
                        l = i - j - k
                        if l > 0 and ((l * l == j * j + k * k) or (k * k == j * j + l * l)):
                                n1 = set()
                                n1.add(j)
                                n1.add(k)
                                n1.add(l)
                                if n1 not in n:
                                        n.append(n1)
        if len(n) > max:
                max = len(n)
                maxp = i

print(maxp)