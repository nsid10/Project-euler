def fifth(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += (int(i))**5
    return sum


sum = 0
for i in range(10, 1000000):
    if fifth(i) == i:
        sum += i
print(sum)
