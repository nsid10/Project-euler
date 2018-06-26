n1 = 0
n2 = 1
f = 0
sum = 0
while f < 4000000:
    f = n1 + n2
    n1 = n2
    n2 = f
    if f % 2 == 0:
        sum += f
print(sum)
