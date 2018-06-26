box = set()
for i in range(2, 101):
    for j in range(2, 101):
        box.add(i**j)
print(len(box))
