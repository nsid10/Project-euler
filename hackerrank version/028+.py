t = int(input().strip())
for x in range(t):
    num = int(input().strip())
    n = (num + 1) // 2
    print(((16 * n**3 - 18 * n**2 + 14 * n) // 3 - 3) % (10**9 + 7))
