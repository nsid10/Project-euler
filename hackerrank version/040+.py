t = int(input())
for x in range(t):
    dn = [int(i) for i in input().split(' ')]
    dn.sort()
    block, exp, prev, product = 0, 0, 0, 1
    for pos in dn:
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
