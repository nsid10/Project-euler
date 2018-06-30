f0, f1, index = 0, 1, 1
while True:
    f0, f1 = f1, f0 + f1
    index += 1
    if len(str(f1)) > 999:
        break
print(index)
