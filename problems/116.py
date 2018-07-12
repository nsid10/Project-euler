from math import factorial as fact

size = 50
ways = 0
for t in [2, 3, 4]:
    for i in range(1, 1 + size // t):
        ways += int(fact(size + i * (1 - t)) / (fact(i) * fact(size - i * t)))
print(ways)
