from itertools import cycle

penta = sum([[i * (3 * i - 1) // 2, i * (3 * i - 1) // 2 + i] for i in range(1, 250)], [])
p = [1] + [0] * 10**6
for n in range(1, 10**6 + 1):
    sign = cycle([1, 1, -1, -1])
    p[n] = sum([p[n - k] * next(sign) for k in penta if n - k >= 0])
    if p[n] % 10**6 == 0:
        break
print(n)
