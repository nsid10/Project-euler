from math import gcd

pMax, tMax = 0, 0
for p in range(1, 1000 + 1):
    t = 0
    for m in range(2, int((p / 2) ** 0.5 + 1)):
        if (p / 2) % m == 0:
            k = m + 1 + m % 2
            while k < 2 * m and k <= p / (2 * m):
                if p / (2 * m) % k == 0 and gcd(k, m) == 1:
                    t += 1
                k += 2
    if t > tMax:
        pMax, tMax = p, t
print(pMax)
