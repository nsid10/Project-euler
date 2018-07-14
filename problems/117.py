from math import factorial as fact

t = 50
ways = 0
for b in range(t // 4 + 1):
    for g in range((t - 4 * b) // 3 + 1):
        for r in range((t - 3 * g - 4 * b) // 2 + 1):
            ways += int(fact(t - r - 2 * g - 3 * b) /
                        (fact(t - 2 * r - 3 * g - 4 * b) * fact(r) * fact(g) * fact(b)))
print(ways)
