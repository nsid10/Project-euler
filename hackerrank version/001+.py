t = int(input().strip())
for i in range(t):
    n = int(input().strip()) - 1
    print((3 * ((n // 3)**2 + (n // 3)) // 2) + (5 * (
        (n // 5)**2 + (n // 5)) // 2) - (15 * ((n // 15)**2 + (n // 15)) // 2))