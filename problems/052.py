def numset(n):
    num = []
    for i in str(n):
        num.append(int(i))
    num.sort()
    return num


n = 1
while True:
    if numset(n) == numset(n * 2) == numset(n * 3) == numset(n * 4) == numset(n * 5) == numset(n * 6):
        break
    n += 1
print(n)
