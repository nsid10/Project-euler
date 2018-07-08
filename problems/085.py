target = 2000000
x, y, area, margin = 2000, 1, 0, target
while x >= y:
    rect = x * (x + 1) * y * (y + 1) // 4
    if abs(target - rect) < margin:
        area = x * y
        margin = abs(target - rect)
    if rect > target:
        x -= 1
    else:
        y += 1
print(area)
