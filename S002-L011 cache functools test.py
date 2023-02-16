import functools
from time import time


@functools.lru_cache(maxsize=3)
def fib(n):
    if n < 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)
    return result


start = time()
[fib(n) for n in range(39)]
print(fib.cache_info())
end = time()

print('Time elapsed:', end - start)
