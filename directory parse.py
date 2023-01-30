import os
from datetime import datetime

my_dic = dict()

with os.scandir('.') as dirs:
    for dir_a in dirs:
        a = (dir_a.name, datetime.utcfromtimestamp(dir_a.stat().st_atime).date().isoformat())
        my_dic[a[0]] = a[1]

print(my_dic)
