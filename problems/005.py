import math


def lcm(box):
    h = box[0]
    for i in range(1, len(box)):
        div = math.gcd(h, box[i])
        h *= box[i] // div
    return h


lcm(list(range(1, 20 + 1)))
