def partition(num):
    ways = []
    for i in range(num + 1):
        ways.append(0)
    ways[0] = 1
    for i in range(1, num + 1):
        for j in range(i, num + 1):
            ways[j] += ways[j - i]
    return ways[-1]


print(partition(100))
