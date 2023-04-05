import itertools
import operator

# Multiplies consecutive numbers in the list
data = [1, 2, 3, 4, 5]
results = itertools.accumulate(data, operator.mul)
for result in results:
    print(result)

# Maximum number by far
data = [1, 4, 3, 6, 5]
results = itertools.accumulate(data, max)
for result in results:
    print(result)

# Cycles through the list of elements
# for d in itertools.cycle(data):
#     print(d)

# Connect two lists as result (elements in sequence)
colors_basic = ['red', 'yellow', 'blue']
colors_mix = ['green', 'orange', 'violet']
results = itertools.chain(colors_basic, colors_mix, data)
for result in results:
    print(result)

# Compress returns values that correspond to True
cars = ['opel', 'skoda']
selection = [False, True]
results = itertools.compress(cars, selection)
for result in results:
    print(result)

# Drop-while/filter-false drops elements that fulfill the requirement
results = itertools.dropwhile(lambda x: x < 5, data)
for result in results:
    print(result)

# Take-while/filter-false drops elements that fulfill the requirement
print('Take-while:')
results = itertools.takewhile(lambda x: x < 5, data)
for result in results:
    print(result)

# Product carthesian multiplier
results = itertools.product(cars, selection)
for result in results:
    print(result)

# Other iterators: repeat, tea, zip_longest - zips longest list filling values with 'fillvalue'.
