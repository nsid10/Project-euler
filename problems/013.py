box = open(
    "D:\Documents\Programming\Python\project euler\p013_large_sum.txt", "r")
numlist = box.read().split()
sum = 0
for i in numlist:
    sum += int(i)
print(sum)
