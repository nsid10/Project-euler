from itertools import cycle

penta = sum([[i * (3 * i - 1) // 2, i * (3 * i - 1) // 2 + i] for i in range(1, 250)], [])
p = [1] + [0] * 60000
for n in range(1, 60000 + 1):
    sign = cycle([1, 1, -1, -1])
    for k in penta:
        if n - k < 0:
            break
        p[n] += p[n - k] * next(sign)

t = int(input())
for x in range(t):
    n = int(input())
    print(p[n] % (10**9 + 7))
