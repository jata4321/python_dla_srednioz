from time import time
import datetime as dt


class Stoper:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args, **kwargs):
        start_time = time()
        result = self.fun(*args, *kwargs.values())
        [print(c) for c in result]
        stop_time = time()
        return print(f'Time lapsed: {stop_time - start_time}')


@Stoper
class DatesFromNow:
    def __init__(self, year, month, day, count):
        self.date = dt.date(year, month, day)
        self.day = day
        self.month = month
        self.year = year
        self.count = count

    def __next__(self):

        if self.count <= 0:
            raise StopIteration()
        else:
            next_day = self.date
            self.date += dt.timedelta(days=1)
            self.count -= 1
        return next_day

    def __iter__(self):
        return self


DatesFromNow(2000, 1, 1, 365)
