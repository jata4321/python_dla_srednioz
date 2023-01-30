import contextlib as ctx
import os
import time

with open('counter.txt', 'r') as file:
    counter = int(file.readline())
    counter += 1

print(counter)

with open('counter.txt', 'w') as file:
    file.writelines(str(counter))

with ctx.suppress(IOError):
    with open('plik*.txt', 'w+') as f:
        f.writelines('Some text')
    os.remove('plik.txt')


class time_me:
    def __init__(self):
        pass

    def __enter__(self):
        # print('entering...')
        self.__start = time.time()
        return print(self.__start)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__stop = time.time()
        self.__diff = self.__stop - self.__start
        return print(self.__diff)


with time_me():
    with time_me() as timer:
        time.sleep(2)
