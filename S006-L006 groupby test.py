import os
import itertools as it

my_path = r'C:\Users\jakub\Documents'


def dir_scan(path):
    with os.scandir(path=path) as iterator:
        for entry in iterator:
            if not entry.is_dir():
                pass
            else:
                yield entry.name


# listing = list(dir_scan(my_path))
listing = dir_scan(my_path)

listing = sorted(listing, key=lambda x: x)
[print(li) for li in listing]

# for is_dir, elements in it.groupby(listing, key=lambda e: e.is_dir()):
#     print(len(elements))
