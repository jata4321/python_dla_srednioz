from datetime import datetime, timedelta, date
import sys


class MillionDays:
    def __init__(self, year, month, day, days):
        self.year = year
        self.month = month
        self.day = day
        self.days = days
        self.date = date(year, month, day)

    def __next__(self):
        if self.days <= 0:
            raise StopIteration
        ret_date = self.date
        self.date += timedelta(days=1)
        self.days -= 1
        return ret_date

    def __iter__(self):
        return self


next_day = MillionDays(2000, 1, 1, 3)
for d in next_day:
    pass

# dates = [date(1100, 1, 1) + timedelta(days=i) for i in range(0, 9)]

# for d in dates:
#     print(d.isoformat())

# print(next(next_day))
# print(next(next_day))
#
# start = datetime.now()
# dates = list(map(lambda d: d.isoformat(), dates))
# stop = datetime.now()
# # print(dates)
# print(sys.getsizeof(dates))
# print(stop - start)
