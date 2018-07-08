target = 200
coinSizes = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0] * target
for i in range(len(coinSizes)):
    for j in range(coinSizes[i], target + 1):
        ways[j] += ways[j - coinSizes[i]]
print(ways[-1])
