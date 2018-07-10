from math import log

box = open("/home/nahian/Documents/Python/p099_base_exp.txt", "r")
pos, line, large = 1, 1, 0
for i in box:
    row = list(map(int, i.split()[0].split(',')))
    if log(row[0]) * row[1] > large:
        large = log(row[0]) * row[1]
        line = pos
    pos += 1
print(line)
