def div(n):
    t = n**0.5
    s = int(-t) if t.is_integer() else 1
    for i in range(2, int(t) + 1):
        if n % i == 0:
            s += i + n // i
    return s


L = 20161
abn = []
for n in range(1, L + 1):
    if div(n) > n:
        abn.append(n)
link = set()
size = len(abn)
for i in range(size):
    if abn[i] > L // 2:
        break
    for j in range(i, size):
        if abn[i] + abn[j] > L:
            break
        link.add(abn[i] + abn[j])
t = int(input())
for x in range(t):
    n = int(input())
    if n > L:
        print('YES')
    elif n in link:
        print('YES')
    else:
        print('NO')
