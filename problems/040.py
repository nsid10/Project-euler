block, exp, prev, product = 0, 0, 0, 1
for pos in [10**i for i in range(7)]:
    while True:
        next = prev + 9 * 10**exp * (exp + 1)
        if pos <= next:
            check = (pos - prev + exp) // (exp + 1)
            product *= int(str(check + block)[(pos - prev + exp) % (exp + 1)])
            break
        block += 9 * 10**exp
        exp += 1
        prev = next
print(product)
