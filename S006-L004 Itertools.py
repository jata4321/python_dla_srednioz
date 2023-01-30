import itertools as it
import random as rnd
import time

mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

start = time.time()
for enum, combination in enumerate(it.combinations_with_replacement(mylist, 59)):
    pass
    # print(enum, combination)

for permutation in enumerate(it.permutations(mylist, 57)):
    pass
    # print(permutation)
end = time.time()

print(end - start)
print(rnd.sample(mylist, 2))
