def path(box):
    size = len(box)
    for x in range(1, size):
        for y in range(size):
            temp = []
            sum = 0
            if y != 0:
                temp.append(box[y][x] + box[y - 1][x])
            for k in range(size - y):
                sum += box[y + k][x]
                if len(temp) > 3:
                    if sum + box[y + k][x - 1] > temp[-1]:
                        break
                temp.append(sum + box[y + k][x - 1])
            box[y][x] = min(temp)
    temp = []
    for i in range(size):
        temp.append(box[i][-1])
    return min(temp)


grid = []
n = int(input())
for grid_i in range(n):
    grid.append([int(grid_temp) for grid_temp in input().split(' ')])
print(path(grid))
