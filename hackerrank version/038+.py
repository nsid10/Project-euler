def pandigital(num, d):
    box = sorted([i for i in str(num)])
    if box == ['1', '2', '3', '4', '5', '6', '7', '8', '9'][:d]:
        return True
    return False


n, k = input().split(' ')
n, k = [int(n), int(k)]
for i in range(2, n):
    m = 1
    pro = ''
    while len(pro) < k:
        pro += str(i * m)
        m += 1
    if pandigital(int(pro), k):
        print(i)
