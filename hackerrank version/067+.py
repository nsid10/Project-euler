def path(a, b):
    c = []
    for i in range(len(a)):
        f1 = a[i] + b[i]
        f2 = a[i] + b[i + 1]
        if f1 > f2:
            c.append(f1)
        else:
            c.append(f2)
    return c


t = int(input())
for x in range(t):
    n = int(input())
    triangle = []
    for y in range(n):
        triangle.append([int(line) for line in input().split(' ')])
    temp = triangle[-1]
    for i in range(len(triangle) - 2, -1, -1):
        temp = path(triangle[i], temp)
    print(temp[0])
