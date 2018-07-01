total = 0
K = int(input())
for i in range(10, 1000000):
    if sum([(int(n))**K for n in str(i)]) == i:
        total += i
print(total)
