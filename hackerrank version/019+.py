def sunday(m, Y):
    if m < 3:
        m += 12
        Y -= 1
        return (1 +
                (13 * m + 13) // 5 + Y + Y // 4 - Y // 100 + Y // 400) % 7 == 1
    return (1 + (13 * m + 13) // 5 + Y + Y // 4 - Y // 100 + Y // 400) % 7 == 1


t = int(input().strip())
for x in range(t):
    Y1, M1, D1 = input().strip().split(' ')
    Y1, M1, D1 = [int(Y1), int(M1), int(D1)]
    Y2, M2, D2 = input().strip().split(' ')
    Y2, M2, D2 = [int(Y2), int(M2), int(D2)]
    days = 0

    if D1 > 1:
        M1 += 1
        if M1 == 13:
            M1 = 1
            Y1 += 1

    for y in range(Y1, Y2 + 1):
        if y == Y1:
            start = M1
        else:
            start = 1
        if y == Y2:
            end = M2
        else:
            end = 12
        for m in range(start, end + 1):
            if sunday(m, y):
                days += 1

    print(days)
