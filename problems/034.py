from math import factorial


def curio(n):
    sum = 0
    for i in str(n):
        sum += factorial(int(i))
    if sum == n:
        return True
    else:
        return False


sum = 0
for i in range(10, 100000):
    if curio(i):
        sum += i
print(sum)
