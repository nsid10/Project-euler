def pandigital(n):
    n = str(n)
    box = []
    for i in n:
        box.append(i)
    box.sort()
    if box == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    return False


def top_digits(n):
    t = n * 0.20898764024997873 + (-0.3494850021680094)
    t = int((pow(10, t - int(t) + 8)))
    return t


fk, f0, f1 = 2, 1, 1
while not pandigital(f1) or not pandigital(top_digits(fk)):
    f0, f1 = f1, (f1 + f0) % 10**9
    fk += 1
print(fk)
