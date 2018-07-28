L = 100000
ds = [1] * L
for i in range(2, int(L**0.5 + 1)):
    for j in range(i + 1, L // i):
        ds[i * j] += i + j
am = []
for i in range(L):
    if ds[i] < i and ds[ds[i]] == i:
        am += [ds[i], i]

t = int(input())
for x in range(t):
    L = int(input())
    print(sum(i for i in am if i < L))
