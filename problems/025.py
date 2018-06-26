f0 = 0
f1 = 1
index = 1
while True:
    f2 = f0 + f1
    f0 = f1
    f1 = f2
    index += 1
    if len(str(f2)) > 999:
        break
print(index)
