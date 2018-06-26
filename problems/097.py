n = 1
for x in range(7830457):
    n *= 2
    if len(str(n)) > 10:
        n = str(n)
        s = n[-10::]
        n = int(s)
n = str(28433 * n + 1)
s = n[-10::]
print(int(s))
