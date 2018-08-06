t = int(input())
for x in range(t):
    n = int(input())
    if ((1 + 8 * n) ** 0.5 - 1) / 2 % 1 == 0:
        print(int(((1 + 8 * n) ** 0.5 - 1) / 2))
    else:
        print(-1)
