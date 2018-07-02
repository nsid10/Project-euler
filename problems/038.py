def pandigital(num):
    box = sorted([i for i in str(num)])
    if box == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    return False


for i in range(10000, 1, -1):
    m = 1
    pro = ''
    while len(pro) < 9:
        pro += str(i * m)
        m += 1
    if pandigital(int(pro)):
        break
print(pro)
