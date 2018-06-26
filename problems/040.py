n = 0
pos = 0
product = 1
exp = 0
while True:
    n += 1
    if exp > 6:
        break
    for i in str(n):
        pos += 1
        if pos == 10**exp:
            product *= int(i)
            exp += 1
print(product)
