from numpy import arange


def primality(n):
    if type(n) != int:
        raise TypeError("argument must be of type 'int'")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5 + 1), 2):
        if n % x == 0:
            return False
    return True


def permutation(box):
    store = [[box[0]]]
    for i in range(1, len(box)):
        temp = []
        for j in store:
            temp += arrange(j, box[i])
        store = list(temp)
    store.sort(reverse=True)
    return store


def arrange(block, e):
    orders = []
    for i in range(len(block) + 1):
        temp = list(block)
        temp.insert(i, e)
        orders.append(temp)
    return orders


flag = False
seed = [7, 4]
for x in seed:
    pan = list(arange(1, x + 1))
    sf = permutation(pan)
    for i in sf:
        num = ''
        for j in i:
            num += str(j)
        k = int(num)
        if primality(k):
            print(k)
            flag = True
            break
    if flag:
        break
