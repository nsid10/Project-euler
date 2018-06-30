from math import factorial

t = int(input().strip())
for x in range(t):
    n = int(input().strip())
    num = str(factorial(n))
    sum = 0
    for i in num:
        sum += int(i)
    print(sum)
