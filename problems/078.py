penta = sum([[i * (3 * i - 1) // 2, i * (3 * i - 1) // 2 + i] for i in range(1, 250)], [])
p = [1] + [0] * 10**6
sign = [1, 1, -1, -1]
for n in range(1, 10**6 + 1):
    for k in range(len(penta)):
        if n - penta[k] < 0:
            break
        p[n] += p[n - penta[k]] * sign[k % 4]
    if p[n] % 10**6 == 0:
        break
print(n)
