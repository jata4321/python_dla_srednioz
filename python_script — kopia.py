print('Hello World!')

from itertools import permutations, combinations_with_replacement
from time import time

ranges = ['A','B','C','D','E','F','G','H']

starter = time()
[print(p) for p in combinations_with_replacement(ranges, 20)]
finisher = time()

print(f'Time lapsed: {finisher-starter}')