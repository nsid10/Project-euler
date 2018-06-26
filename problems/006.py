nums = 100
sum_sq = 0
for i in range(1, nums + 1):
    sum_sq = sum_sq + i**2
sum = 0
for i in range(1, nums + 1):
    sum += i
sq_sum = sum**2
print(sq_sum - sum_sq)
