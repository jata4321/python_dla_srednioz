import datetime

net = 1200
gross = 1000
assert net > gross, 'Please check gross/net.'

order_date = datetime.date(2020, 1, 1)
current_date = datetime.date.today()
assert order_date <= current_date, 'Order date must be before current date'

print('\n', order_date, '\n', current_date)
