from math import factorial as fact


def primality(n):
    if type(n) != int:
        raise TypeError("argument must be of type 'int'")
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5 + 1), 2):
        if n % i == 0:
            return False
    return True


store = []
flag = False
for d in [7, 4]:
    for pos in range(fact(d), 0, -1):
        num = ['1', '2', '3', '4', '5', '6', '7', '8', '9'][:d]
        box = ''
        while len(num) > 0:
            size = fact(len(num)) // len(num)
            box += num[(pos - 1) // size]
            num.pop((pos - 1) // size)
            while pos >= size:
                pos -= size
        if primality(int(box)):
            store.append(int(box))
t = int(input())
for x in range(t):
    n = int(input())
    for i in store:
        if i <= n:
            print(i)
            break
    else:
        print(-1)
