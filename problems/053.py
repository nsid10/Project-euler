from math import factorial


def combination(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n - r)))


count = 0
for n in range(1, 101):
    for r in range(n + 1):
        if combination(n, r) > 1000000:
            count += 1
print(count)
