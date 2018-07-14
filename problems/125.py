def palindrome(num):
    num = str(num)
    if num == num[::-1]:
        return True
    return False


target = 10**8
box = [i**2 for i in range(1, int((target / 2)**0.5))]
size = len(box)
store = set()
for i in range(size, 1, -1):
    for j in range(size - i + 1):
        sqsum = sum(box[j:i + j])
        if sqsum > target:
            break
        elif palindrome(sqsum):
            store.add(sqsum)
print(sum(store))
