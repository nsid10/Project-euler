from math import factorial

n = 20 + 20
r = 20
paths = int(factorial(n) / (factorial(r) * factorial(n - r)))
print(paths)
