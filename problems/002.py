n1, n2, sum = 0, 1, 0
while n2 < 4000000:
    n1, n2 = n2, n1 + n2
    if n2 % 2 == 0:
        sum += n2
print(sum)
