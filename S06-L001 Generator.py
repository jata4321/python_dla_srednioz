import datetime as dt


def million_days(year, month, day, maxdays):
    date = dt.date(year, month, day)
    for i in range(maxdays):
        yield date + dt.timedelta(days=1)  # yield instead of return


for d in million_days(2022, 1, 1, 3):
    print(d)
