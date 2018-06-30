# ---using datetime------------------------------------------------------------
import datetime as dt
sundays = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if dt.date(year, month, 1).isoweekday() == 7:
            sundays += 1
print(sundays)


# ---using Zeller's congruence ------------------------------------------------
def sunday(m, Y):
    if m < 3:
        m += 12
        Y -= 1
        return (1 +
                (13 * m + 13) // 5 + Y + Y // 4 - Y // 100 + Y // 400) % 7 == 1
    return (1 + (13 * m + 13) // 5 + Y + Y // 4 - Y // 100 + Y // 400) % 7 == 1


days = 0
for y in range(1901, 2001):
    for m in range(1, 13):
        if sunday(m, y):
            days += 1
print(days)
