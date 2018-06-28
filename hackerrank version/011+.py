grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)
large = 0
for y in range(20):
    for x in range(20 - 3):
        product = 1
        for k in range(4):
            product *= grid[y][x + k]
        if product > large:
            large = product
        product = 1
        for k in range(4):
            product *= grid[x + k][y]
        if product > large:
            large = product
for y in range(20 - 3):
    for x in range(20 - 3):
        product = 1
        for k in range(4):
            product *= grid[y + k][x + k]
        if product > large:
            large = product
        product = 1
        for k in range(4):
            product *= grid[y + k][x - k + 3]
        if product > large:
            large = product
print(large)
