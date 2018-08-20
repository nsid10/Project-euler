penta = set()
i = 1000
while i is not False:
    i += 1
    s = (3 * i * i - i) // 2
    for j in penta:
        if s - j in penta and s - 2 * j in penta:
            i = False
            break
    penta.add(s)
print(s - 2 * j)
