from math import log

box = open("D:\Documents\Programming\Python\project euler\p099_base_exp.txt", "r")
pos = 1
line = 1
large = 0
for i in box:
    row = i.split()
    row = list(map(int, row[0].split(',')))
    if log(row[0]) * row[1] > large:
        large = log(row[0]) * row[1]
        line = pos
    pos += 1
print(line)
