d = 1
for i in range(10):
    for j in range(1, i):
        q, r = divmod(9 * i * j, 10 * j - i)
        if r == 0 and q < 10:
            d *= i / j
print(int(d))
