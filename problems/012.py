n = 1
while True:
    div = 0
    tri = (n**2 + n) / 2
    n += 1
    for i in range(1, int(tri**0.5 + 1)):
        if tri % i == 0:
            div += 1
    div *= 2
    if (tri**0.5) % 1 == 0:
        div -= 1
    if div > 500:
        break
print(int(tri))
