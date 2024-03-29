import itertools as it
import math
from itertools import combinations_with_replacement, combinations, permutations
from math import factorial, pow
import time

start = time.time()
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C#', 'D#', 'G#', 'F#', 'A#']
notes_set = 12

# for enum, combination in enumerate(permutations(notes, notes_set)):
#     pass
#
# print(enum)
#
# combination_number = factorial(len(notes)) / factorial(len(notes) - notes_set)
# print(combination_number)

# notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

for x in it.permutations(notes, 10):
    print(x)

print("4-notes melody, notes cannot repeat - it is variation without repeating - there are {} possibilities".format(
    math.factorial(len(notes)) / math.factorial(len(notes) - 4)))
end = time.time()
print(f"Time elapsed: {end - start}")
# input('Press enter')
#
# for x in it.product(notes, repeat=4):
#     print(x)
#
# print("4-notes melody - notes can repeat - it is variation with repeating - there are {} possibilities".format(
#     pow(len(notes), 4)))
