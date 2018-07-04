n, d = input().split(' ')
n, d = [int(n), int(d)]
numbers = [0] * (n + d)
for i in range(2, n + d):
    if numbers[i] == d:
        c += 1
        if c == d:
            print(i - d + 1)
            c -= 1
    else:
        c = 0
        if numbers[i] == 0:
            numbers[i::i] = [x + 1 for x in numbers[i::i]]
