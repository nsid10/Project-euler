flag = False
for m in range(1000):
    for n in range(m):
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2
        if (a + b + c) == 1000:
            flag = True
            break
    if flag:
        break
print(a * b * c)
