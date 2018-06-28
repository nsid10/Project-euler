from math import factorial as fact

t = int(input().strip())
for x in range(t):
    m, n = input().strip().split(' ')
    m, n = int(m), int(n)
    print((fact(m + n) // (fact(m) * fact(n))) % (10**9 + 7))
