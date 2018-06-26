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


box = open("D:\Documents\Programming\Python\project euler\p067_triangle.txt", "r")
numlist = box.read().split('\n')
numlist.pop(-1)
triangle = []
for i in numlist:
    temp = []
    for j in i.split():
        temp.append(int(j))
    triangle.append(temp)
temp = triangle[-1]
for i in range(len(triangle) - 2, -1, -1):
    temp = path(triangle[i], temp)
print(temp[0])
