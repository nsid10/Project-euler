def permute(n):
    n = str(n)
    box = []
    for i in n:
        box.append(i)
    box.sort()
    num = ''
    for i in box:
        num += i
    return num


i = 1
limit = 10
cubes = {}
while True:
    i += 1
    num = i**3
    if num > limit:
        limit *= 10
        cubes = {}
    box = permute(num)
    if box not in cubes:
        cubes[box] = [1, num]
    else:
        cubes[box][0] += 1
        if cubes[box][0] == 5:
            break
print(cubes[box][1])
