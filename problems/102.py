with open("/home/nahian/Documents/Python/p102_triangles.txt", "r") as box:
    gridlist = box.read().split()

count = 0
for tri in gridlist:
    x1, y1, x2, y2, x3, y3 = [int(va) for va in tri.split(',')]
    area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
    area1 = abs((x2 * y3 - x3 * y2) / 2)
    area2 = abs((x3 * y1 - x1 * y3) / 2)
    area3 = abs((x1 * y2 - x2 * y1) / 2)
    if area == area1 + area2 + area3:
        count += 1
print(count)
