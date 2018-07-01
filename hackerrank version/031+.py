coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [0]
for i in range(10**5):
    ways += [0]
ways[0] = 1
for i in range(len(coins)):
    for j in range(coins[i], 10**5 + 1):
        ways[j] += ways[j - coins[i]]

t = int(input())
for x in range(t):
    n = int(input())
    print(ways[n] % (10**9 + 7))
