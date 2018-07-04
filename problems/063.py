n = 0
count = 0
while n < 25:
    n += 1
    i = 0
    while i < 10:
        i += 1
        if len(str(i**n)) == n:
            count += 1
print(count)
