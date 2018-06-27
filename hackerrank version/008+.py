t = int(input().strip())
for x in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    box = input().strip()
    large = 0
    for i in range(0, n + 1 - k):
        cache = 1
        for j in range(k):
            cache *= int(box[i + j])
        if cache > large:
            large = cache
    print(large)
