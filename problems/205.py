def dice(sides, rolls):
    face = {}
    for i in range(sides):
        face[i + 1] = 1
    dist = dict(face)
    for i in range(1, rolls):
        temp = {}
        for j in face:
            for k in dist:
                if j + k not in temp:
                    temp[j + k] = dist[k]
                else:
                    temp[j + k] += dist[k]
        dist = dict(temp)
    return dist


tetra = dice(4, 9)
cube = dice(6, 6)
wins = 0
total = 0
for i in tetra:
    for j in cube:
        if i > j:
            wins += tetra[i] * cube[j]
        total += tetra[i] * cube[j]
print(round(wins / total, 7))
