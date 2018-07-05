ways = [1] + [0] * 100
for i in range(1, 101):
    for j in range(i, 101):
        ways[j] += ways[j - i]
print(ways[-1] - 1)
