from numpy import arange


def permutation(box):
    store = [[box[0]]]
    for i in range(1, len(box)):
        temp = []
        for j in store:
            temp += arrange(j, box[i])
        store = list(temp)
    store.sort()
    return store


def arrange(block, e):
    orders = []
    for i in range(len(block) + 1):
        temp = list(block)
        temp.insert(i, e)
        orders.append(temp)
    return orders


pan = list(arange(9 + 1))
print(pan)
print(permutation(pan)[1000000 - 1])
