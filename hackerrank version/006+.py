t = int(input().strip())
for x in range(t):
    n = int(input().strip())
    print(((n**2+n)//2)**2 - (2 * n**3 + 3 * n**2 + n) // 6)
