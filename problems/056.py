def digitsum(n):
    new = str(n)
    sum = 0
    for i in new:
        sum += int(i)
    return sum


large = 0
for a in range(1, 100):
    for b in range(1, 100):
        if large < digitsum(a**b):
            large = digitsum(a**b)
print(large)
