from math import log

exp = []
t = int(input())
for x in range(t):
    b, e = [int(va) for va in input().split(' ')]
    exp.append(int(str(round(log(b) * e * 10**5)) + str(10**10 + b)[-10::] + str(10**10 + e)[-10::]))
exp.sort()
big = str(exp[int(input()) - 1])
print(int(big[-20:-10:]), int(big[-10::]))
