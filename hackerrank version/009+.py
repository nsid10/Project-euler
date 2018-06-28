def divisors(n):
    for divisor in range(1, int(n**0.5) + 1):
        if n % divisor == 0:
            yield divisor, n // divisor


pn = {}
for r in range(2, 550, 2):
    st = r**2 // 2
    for s, t in divisors(st):
        A = (r + s) + (r + t) + (r + s + t)
        pn[A] = (r + s) * (r + t) * (r + s + t)

t = int(input().strip())
for x in range(t):
    A = int(input().strip())
    print(pn[A] if A in pn else -1)
