n = 1001
limit = int((n + 1) / 2)
num = -3
for n in range(1, limit + 1):
    num += (16 * (n**2) - 28 * n + 16)
print(num)
