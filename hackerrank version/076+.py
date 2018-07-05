ways = []
for i in range(1001):
    ways.append(0)
ways[0] = 1
for i in range(1, 1001):
    for j in range(i, 1001):
        ways[j] += ways[j - i]
t = int(input())
for x in range(t):
    n = int(input())
    print((ways[n] - 1) % (10**9 + 7))
