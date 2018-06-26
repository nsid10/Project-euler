long = 0
start = 0
for n in range(1, 1000000):
    chain = 1
    t = n
    while t > 1:
        if t % 2 == 0:
            t /= 2
            chain += 1
        else:
            t = 3 * t + 1
            chain += 1
    if chain > long:
        long = chain
        start = n
print(start)
