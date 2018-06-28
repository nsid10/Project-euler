with open("/home/nahian/Documents/Python/p013_large_sum.txt", "r") as box:
    numlist = box.read().split()
sum = 0
for i in numlist:
    sum += int(i)
print(str(sum)[:10])
