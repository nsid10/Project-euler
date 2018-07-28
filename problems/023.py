def div(n):
    t = n**0.5
    s = int(-t) if t.is_integer() else 1
    for i in range(2, int(t) + 1):
        if n % i == 0:
            s += i + n // i
    return s


L, s = 20161, 0
abn = set()
for n in range(1, L + 1):
    if div(n) > n:
        abn.add(n)
    if not any((n - a in abn) for a in abn):
        s += n
print(s)
