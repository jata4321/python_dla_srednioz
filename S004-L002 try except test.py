import datetime as dt


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_date(self):
        if len(self.title) == 0:
            raise Exception("Title is empty!")
        if self.start > self.end:
            raise ValueError("Start date is later than end date!")

    @classmethod
    def publish_offer(cls, trip):
        list_of_errors = list()
        try:
            if len(trip) == 0:
                raise Exception('No trips in list')
            for i, t in enumerate(trip):
                try:
                    t.check_date()
                except ValueError as e:
                    list_of_errors.append({i-1: [t.title, e]})
            if len(list_of_errors) > 0:
                raise ValueError
        except ValueError:
            print('List is corrupt.', list_of_errors)
        except Exception as e:
            print(e)
        else:
            print('List OK.')


trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]

Trip.publish_offer(trips)
