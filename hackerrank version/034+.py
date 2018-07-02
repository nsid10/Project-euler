from math import factorial


def curio(n):
    sum = 0
    for i in str(n):
        sum += factorial(int(i))
    if sum % n == 0:
        return True
    return False


N = int(input())
sum = 0
for i in range(10, N):
    if curio(i):
        sum += i
print(sum)
