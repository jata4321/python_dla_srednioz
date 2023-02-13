from time import time
import functools


def wrapper_time(a_function):
    def a_wrapped_function(*args, **kwargs):
        start_time = time()
        result = a_function(*args, **kwargs)
        end_time = time()
        print(end_time - start_time)
        return result

    return a_wrapped_function


@wrapper_time
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


# new_fun = wrapper_time(get_sequence)
#
# print(new_fun(19))

print(get_sequence(3))
