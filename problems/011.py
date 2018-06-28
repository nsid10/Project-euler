with open("/home/nahian/Documents/Python/p011_grid.txt", "r") as box:
    gridlist = box.read().split()
grid = []
pos = 0
for i in range(20):
    row = []
    for j in range(20):
        row.append(int(gridlist[pos]))
        pos += 1
    grid.append(row)
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
