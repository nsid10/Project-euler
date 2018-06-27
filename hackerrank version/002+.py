t = int(input().strip())
for i in range(t):
    target = int(input().strip())
    n1, n2, sum = 0, 1, 0
    while n2 < target:
        if n2 % 2 == 0:
            sum += n2
        n1, n2 = n2, n1 + n2
    print(sum)
