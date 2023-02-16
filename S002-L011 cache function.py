from time import time
import functools


@functools.lru_cache()
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


start = time()
for i in range(1, 999):
    print(f'{i}! : {factorial(i)}')
end = time()
print('Time elapsed:', end - start)
