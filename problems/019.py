import datetime as dt
sundays = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if dt.date(year, month, 1).isoweekday() == 7:
            sundays += 1
print(sundays)
