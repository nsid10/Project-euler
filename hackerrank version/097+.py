big = 0
t = int(input())
for x in range(t):
    a, b, c, d = [int(va) for va in input().split(' ')]
    big += a * pow(b, c, 10**12) + d

print(str(10**12 + big)[-12::])
