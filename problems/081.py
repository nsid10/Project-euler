def path(box):
    for i in range(1, len(box[0])):
        box[0][i] += box[0][i - 1]
    size = len(box)
    for i in range(1, size):
        box[i][0] += box[i - 1][0]
        for j in range(1, size):
            if box[i][j - 1] < box[i - 1][j]:
                box[i][j] += box[i][j - 1]
            else:
                box[i][j] += box[i - 1][j]
    return box[-1][-1]


box = open("D:\Documents\Programming\Python\project euler\p081_matrix.txt", "r")
table = box.read().split()
mat = []
for i in table:
    row = i.split(',')
    for j in range(len(row)):
        row[j] = int(row[j])
    mat.append(row)
print(path(mat))
