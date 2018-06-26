def conceal(num):
    num = str(num)
    for i in range(1, 10):
        if int(num[2 * (i - 1)]) != i:
            return False
    return True


for i in range(138902663, 101010103, -2):
    if conceal(i**2):
        print(i * 10)
        break
